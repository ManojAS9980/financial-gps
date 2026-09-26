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


def get_company_data(symbol):
    """
    Fetch company information, financial statement data,
    and basic calculated financial ratios.
    """
    try:
        ticker = yf.Ticker(symbol)

        info = ticker.info
        income = ticker.income_stmt
        balance = ticker.balance_sheet
        cashflow = ticker.cashflow

        company_data = {
            "name": info.get("longName", "Not available"),
            "price": info.get("currentPrice"),
            "market_cap": info.get("marketCap"),
            "sector": info.get("sector", "Not available"),
            "industry": info.get("industry", "Not available"),

            "revenue": get_latest_value(
                income,
                ["Total Revenue", "Operating Revenue"]
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
            )
        }

        # -------------------------------
        # Calculate ROE
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
        # Calculate ROCE
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
        # Calculate Debt-to-Equity
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