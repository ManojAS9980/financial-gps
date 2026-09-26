import yfinance as yf
import pandas as pd


def get_latest_value(statement, possible_names):
    """
    Get the latest available value for a financial statement item.
    """
    if statement is None or statement.empty:
        return None

    for name in possible_names:
        if name in statement.index:
            row = statement.loc[name]

            for value in row:
                if pd.notna(value):
                    return float(value)

    return None


def get_latest_two_values(statement, possible_names):
    """
    Get the latest two available values for a financial statement item.
    Returns:
        (latest_value, previous_value)
    """
    if statement is None or statement.empty:
        return None, None

    for name in possible_names:
        if name in statement.index:
            row = statement.loc[name]

            values = []

            for value in row:
                if pd.notna(value):
                    values.append(float(value))

            if len(values) >= 2:
                return values[0], values[1]

    return None, None


def calculate_growth(latest, previous):
    """
    Calculate percentage growth between two values.
    """
    if latest is None or previous in (None, 0):
        return None

    return ((latest - previous) / previous) * 100


def get_company_data(symbol):
    """
    Fetch company information, financial data,
    and calculated financial ratios.
    """
    try:
        ticker = yf.Ticker(symbol)

        info = ticker.info
        income = ticker.income_stmt
        balance = ticker.balance_sheet
        cashflow = ticker.cashflow

        # -------------------------------
        # Basic company information
        # -------------------------------
        price = info.get("currentPrice")

        if price is None:
            price = info.get("regularMarketPrice")

        company_data = {
            "name": info.get("longName", "Not available"),
            "price": price,
            "market_cap": info.get("marketCap"),
            "sector": info.get("sector", "Not available"),
            "industry": info.get("industry", "Not available"),

            # -------------------------------
            # Financial statement data
            # -------------------------------
            "revenue": get_latest_value(
                income,
                [
                    "Total Revenue",
                    "Operating Revenue"
                ]
            ),

            "net_income": get_latest_value(
                income,
                [
                    "Net Income",
                    "Net Income Common Stockholders"
                ]
            ),

            "ebit": get_latest_value(
                income,
                [
                    "EBIT",
                    "Operating Income"
                ]
            ),

            "total_debt": get_latest_value(
                balance,
                ["Total Debt"]
            ),

            "equity": get_latest_value(
                balance,
                [
                    "Stockholders Equity",
                    "Common Stock Equity",
                    "Total Equity Gross Minority Interest"
                ]
            ),

            "operating_cash_flow": get_latest_value(
                cashflow,
                [
                    "Operating Cash Flow",
                    "Total Cash From Operating Activities"
                ]
            ),

            "free_cash_flow": get_latest_value(
                cashflow,
                ["Free Cash Flow"]
            ),

            "eps": info.get("trailingEps")
        }

        # -------------------------------
        # Revenue Growth
        # -------------------------------
        latest_revenue, previous_revenue = get_latest_two_values(
            income,
            [
                "Total Revenue",
                "Operating Revenue"
            ]
        )

        company_data["revenue_growth"] = calculate_growth(
            latest_revenue,
            previous_revenue
        )

        # -------------------------------
        # Profit Growth
        # -------------------------------
        latest_profit, previous_profit = get_latest_two_values(
            income,
            [
                "Net Income",
                "Net Income Common Stockholders"
            ]
        )

        company_data["profit_growth"] = calculate_growth(
            latest_profit,
            previous_profit
        )

        # -------------------------------
        # P/E Ratio
        # -------------------------------
        if (
            company_data["price"] is not None
            and company_data["eps"] is not None
            and company_data["eps"] > 0
        ):
            company_data["pe_ratio"] = (
                company_data["price"]
                / company_data["eps"]
            )
        else:
            company_data["pe_ratio"] = None

        # -------------------------------
        # ROE
        # -------------------------------
        if (
            company_data["net_income"] is not None
            and company_data["equity"] not in (None, 0)
        ):
            company_data["roe"] = (
                company_data["net_income"]
                / company_data["equity"]
            ) * 100
        else:
            company_data["roe"] = None

        # -------------------------------
        # ROCE
        # Simplified educational version
        # -------------------------------
        if (
            company_data["ebit"] is not None
            and company_data["equity"] is not None
        ):
            debt = company_data["total_debt"] or 0

            capital_employed = (
                company_data["equity"] + debt
            )

            if capital_employed > 0:
                company_data["roce"] = (
                    company_data["ebit"]
                    / capital_employed
                ) * 100
            else:
                company_data["roce"] = None
        else:
            company_data["roce"] = None

        # -------------------------------
        # Debt-to-Equity
        # -------------------------------
        if (
            company_data["total_debt"] is not None
            and company_data["equity"] not in (None, 0)
        ):
            company_data["debt_to_equity"] = (
                company_data["total_debt"]
                / company_data["equity"]
            )
        else:
            company_data["debt_to_equity"] = None

        return company_data

    except Exception as error:
        print(f"\n❌ Could not fetch company data: {error}")
        return None