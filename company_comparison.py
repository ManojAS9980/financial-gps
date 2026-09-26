from market_data import get_company_data


def format_number(value, symbol):
    """Format large financial values with a currency symbol."""
    if value is None:
        return "N/A"

    return f"{symbol}{value:,.0f}"


def format_price(value, symbol):
    """Format share price."""
    if value is None:
        return "N/A"

    return f"{symbol}{value:,.2f}"


def format_ratio(value):
    """Format a ratio."""
    if value is None:
        return "N/A"

    return f"{value:.2f}"


def format_percent(value):
    """Format a percentage."""
    if value is None:
        return "N/A"

    return f"{value:.2f}%"


def compare_companies():
    print("\n========== COMPANY COMPARISON ==========")

    symbol1 = input(
        "\nEnter first stock symbol (example: TCS.NS): "
    ).strip().upper()

    symbol2 = input(
        "Enter second stock symbol (example: INFY.NS): "
    ).strip().upper()

    if not symbol1 or not symbol2:
        print("\n❌ Both stock symbols are required.")
        return

    print("\nFetching company data...")
    print(f"Fetching {symbol1}...")
    company1 = get_company_data(symbol1)

    print(f"Fetching {symbol2}...")
    company2 = get_company_data(symbol2)

    if company1 is None or company2 is None:
        print("\n❌ Could not retrieve data for both companies.")
        return

    currency1 = company1["financial_symbol"]
    currency2 = company2["financial_symbol"]

    price_symbol1 = company1["price_symbol"]
    price_symbol2 = company2["price_symbol"]

    print("\n========== SIDE-BY-SIDE COMPARISON ==========")

    print(f"\n{'Metric':<25} {symbol1:<22} {symbol2:<22}")
    print("-" * 70)

    print(
        f"{'Company':<25} "
        f"{company1['name'][:20]:<22} "
        f"{company2['name'][:20]:<22}"
    )

    print(
        f"{'Sector':<25} "
        f"{company1['sector']:<22} "
        f"{company2['sector']:<22}"
    )

    print("\n---------- Market Data ----------")

    print(
        f"{'Current Price':<25} "
        f"{format_price(company1['price'], price_symbol1):<22} "
        f"{format_price(company2['price'], price_symbol2):<22}"
    )

    print(
        f"{'Market Cap':<25} "
        f"{format_number(company1['market_cap'], price_symbol1):<22} "
        f"{format_number(company2['market_cap'], price_symbol2):<22}"
    )

    print("\n---------- Financial Data ----------")

    print(
        f"{'Financial Currency':<25} "
        f"{company1['financial_currency']:<22} "
        f"{company2['financial_currency']:<22}"
    )

    print(
        f"{'Revenue':<25} "
        f"{format_number(company1['revenue'], currency1):<22} "
        f"{format_number(company2['revenue'], currency2):<22}"
    )

    print(
        f"{'Net Income':<25} "
        f"{format_number(company1['net_income'], currency1):<22} "
        f"{format_number(company2['net_income'], currency2):<22}"
    )

    print(
        f"{'Total Debt':<25} "
        f"{format_number(company1['total_debt'], currency1):<22} "
        f"{format_number(company2['total_debt'], currency2):<22}"
    )

    print(
        f"{'Equity':<25} "
        f"{format_number(company1['equity'], currency1):<22} "
        f"{format_number(company2['equity'], currency2):<22}"
    )

    print("\n---------- Valuation & Ratios ----------")

    print(
        f"{'Trailing EPS':<25} "
        f"{format_price(company1['eps'], price_symbol1):<22} "
        f"{format_price(company2['eps'], price_symbol2):<22}"
    )

    print(
        f"{'Trailing P/E':<25} "
        f"{format_ratio(company1['pe_ratio']):<22} "
        f"{format_ratio(company2['pe_ratio']):<22}"
    )

    print(
        f"{'ROE':<25} "
        f"{format_percent(company1['roe']):<22} "
        f"{format_percent(company2['roe']):<22}"
    )

    print(
        f"{'ROCE':<25} "
        f"{format_percent(company1['roce']):<22} "
        f"{format_percent(company2['roce']):<22}"
    )

    print(
        f"{'Debt-to-Equity':<25} "
        f"{format_ratio(company1['debt_to_equity']):<22} "
        f"{format_ratio(company2['debt_to_equity']):<22}"
    )

    print("\n---------- Growth ----------")

    print(
        f"{'Revenue Growth':<25} "
        f"{format_percent(company1['revenue_growth']):<22} "
        f"{format_percent(company2['revenue_growth']):<22}"
    )

    print(
        f"{'Profit Growth':<25} "
        f"{format_percent(company1['profit_growth']):<22} "
        f"{format_percent(company2['profit_growth']):<22}"
    )

    print(
        "\nNote: Financial statement values are shown "
        "in each company's reporting currency."
    )

    print(
        "Direct comparison of monetary amounts across "
        "different currencies requires currency conversion."
    )