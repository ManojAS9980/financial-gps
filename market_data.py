import yfinance as yf
import pandas as pd


def get_latest_value(statement, possible_names):
    """
    Find the latest available value for a financial statement item.
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
    Fetch basic company information and selected financial data.
    """
    try:
        ticker = yf.Ticker(symbol)

        info = ticker.info

        # Get financial statements
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
                ["Net Income", "Net Income Common Stockholders"]
            ),

            "ebit": get_latest_value(
                income,
                ["EBIT", "Operating Income"]
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

            "free_cash_flow": get_latest_value(
                cashflow,
                ["Free Cash Flow"]
            ),

            "operating_cash_flow": get_latest_value(
                cashflow,
                [
                    "Operating Cash Flow",
                    "Total Cash From Operating Activities"
                ]
            ),
        }

        return company_data

    except Exception as error:
        print(f"\n❌ Could not fetch company data: {error}")
        return None