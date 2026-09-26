import yfinance as yf
import pandas as pd


def get_historical_series(statement, possible_names):
    """
    Get annual values for a financial statement item.

    Returns:
        Dictionary in the form:
        {year: value}
    """
    if statement is None or statement.empty:
        return {}

    for name in possible_names:
        if name in statement.index:
            row = statement.loc[name]
            result = {}

            for column, value in row.items():
                if pd.notna(value):
                    year = pd.Timestamp(column).year
                    result[year] = float(value)

            return result

    return {}


def calculate_growth(current, previous):
    """
    Calculate percentage growth.
    """
    if current is None or previous in (None, 0):
        return None

    return ((current - previous) / previous) * 100


def format_amount(value, symbol):
    """
    Format a financial amount.
    """
    if value is None:
        return "N/A"

    return f"{symbol}{value:,.0f}"


def show_historical_trends(symbol):
    """
    Display a multi-year financial trend for a company.
    """
    print("\n========== HISTORICAL TRENDS ==========")
    print(f"Fetching historical data for {symbol}...")

    try:
        ticker = yf.Ticker(symbol)

        info = ticker.info
        income = ticker.income_stmt

        if income is None or income.empty:
            print("\n❌ Historical financial data is not available.")
            return

        financial_currency = info.get(
            "financialCurrency",
            info.get("currency", "N/A")
        )

        currency_symbols = {
            "INR": "₹",
            "USD": "$",
            "EUR": "€",
            "GBP": "£",
            "JPY": "¥",
            "CNY": "¥",
            "AUD": "A$",
            "CAD": "C$",
            "SGD": "S$",
            "HKD": "HK$"
        }

        symbol_sign = currency_symbols.get(
            financial_currency,
            financial_currency
        )

        company_name = info.get(
            "longName",
            symbol
        )

        revenue = get_historical_series(
            income,
            [
                "Total Revenue",
                "Operating Revenue"
            ]
        )

        net_income = get_historical_series(
            income,
            [
                "Net Income",
                "Net Income Common Stockholders"
            ]
        )

        ebit = get_historical_series(
            income,
            [
                "EBIT",
                "Operating Income"
            ]
        )

        all_years = set()

        all_years.update(revenue.keys())
        all_years.update(net_income.keys())
        all_years.update(ebit.keys())

        if not all_years:
            print("\n❌ No usable historical data was found.")
            return

        years = sorted(all_years)[-4:]

        print(f"\nCompany: {company_name}")
        print(f"Financial Currency: {financial_currency}")

        print("\n---------- Annual Financial Trend ----------")

        header = (
            f"{'Metric':<20}"
            + "".join(f"{year:<18}" for year in years)
        )

        print(header)
        print("-" * len(header))

        # Revenue
        revenue_row = f"{'Revenue':<20}"

        for year in years:
            value = revenue.get(year)
            revenue_row += f"{format_amount(value, symbol_sign):<18}"

        print(revenue_row)

        # Net Income
        profit_row = f"{'Net Income':<20}"

        for year in years:
            value = net_income.get(year)
            profit_row += f"{format_amount(value, symbol_sign):<18}"

        print(profit_row)

        # EBIT
        ebit_row = f"{'EBIT':<20}"

        for year in years:
            value = ebit.get(year)
            ebit_row += f"{format_amount(value, symbol_sign):<18}"

        print(ebit_row)

        # Latest revenue growth
        revenue_years = sorted(revenue.keys())

        if len(revenue_years) >= 2:
            latest_revenue_year = revenue_years[-1]
            previous_revenue_year = revenue_years[-2]

            latest_revenue = revenue[latest_revenue_year]
            previous_revenue = revenue[previous_revenue_year]

            revenue_growth = calculate_growth(
                latest_revenue,
                previous_revenue
            )

            print(
                f"\nRevenue Growth "
                f"({previous_revenue_year} → "
                f"{latest_revenue_year}): "
                f"{revenue_growth:.2f}%"
            )

        else:
            print("\nRevenue Growth: Not available")

        # Latest profit growth
        profit_years = sorted(net_income.keys())

        if len(profit_years) >= 2:
            latest_profit_year = profit_years[-1]
            previous_profit_year = profit_years[-2]

            latest_profit = net_income[latest_profit_year]
            previous_profit = net_income[previous_profit_year]

            profit_growth = calculate_growth(
                latest_profit,
                previous_profit
            )

            print(
                f"Profit Growth "
                f"({previous_profit_year} → "
                f"{latest_profit_year}): "
                f"{profit_growth:.2f}%"
            )

        else:
            print("\nProfit Growth: Not available")

        print(
            "\nNote: Historical values depend on the "
            "financial data available from the data source."
        )

    except Exception as error:
        print(
            f"\n❌ Could not fetch historical data: {error}"
        )