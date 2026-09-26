import yfinance as yf


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_latest_value(statement, possible_names):
    """
    Get the latest available numeric value from a financial statement.
    """

    if statement is None or statement.empty:
        return None

    for name in possible_names:

        if name in statement.index:

            row = statement.loc[name]

            for value in row:
                if value is not None:
                    try:
                        if value == value:  # filters NaN
                            return float(value)
                    except (TypeError, ValueError):
                        continue

    return None


def get_latest_two_values(statement, possible_names):
    """
    Get the latest two available numeric values from a financial statement.
    """

    if statement is None or statement.empty:
        return None, None

    for name in possible_names:

        if name in statement.index:

            row = statement.loc[name]

            values = []

            for value in row:
                if value is not None:
                    try:
                        numeric_value = float(value)

                        if numeric_value == numeric_value:
                            values.append(numeric_value)
                    except (TypeError, ValueError):
                        continue

            if len(values) >= 2:
                return values[0], values[1]

            if len(values) == 1:
                return values[0], None

    return None, None


def calculate_growth(latest, previous):
    """
    Calculate percentage growth between two values.
    """

    if latest is None or previous is None:
        return None

    if previous == 0:
        return None

    return ((latest - previous) / abs(previous)) * 100


def get_currency_symbol(currency):
    """
    Convert a currency code into a display symbol.
    """

    symbols = {
        "INR": "₹",
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥",
        "CNY": "¥",
        "AUD": "A$",
        "CAD": "C$",
        "SGD": "S$",
        "HKD": "HK$",
    }

    if currency is None:
        return ""

    return symbols.get(currency.upper(), currency + " ")


# ============================================================
# COMPANY DATA
# ============================================================

def get_company_data(symbol):
    """
    Fetch company information and financial metrics using yfinance.
    """

    try:
        ticker = yf.Ticker(symbol)

        # ----------------------------------------------------
        # BASIC COMPANY INFORMATION
        # ----------------------------------------------------

        info = ticker.info

        name = info.get("longName") or info.get("shortName") or symbol

        price = info.get("currentPrice")

        # Fallback for current price
        if price is None:
            try:
                fast_info = ticker.fast_info
                price = fast_info.get("last_price")
            except Exception:
                price = None

        market_cap = info.get("marketCap")

        sector = info.get("sector", "N/A")
        industry = info.get("industry", "N/A")

        # ----------------------------------------------------
        # CURRENCIES
        # ----------------------------------------------------

        listing_currency = info.get("currency") or "USD"

        financial_currency = (
            info.get("financialCurrency")
            or listing_currency
        )

        price_symbol = get_currency_symbol(listing_currency)

        financial_symbol = get_currency_symbol(financial_currency)

        # ----------------------------------------------------
        # FINANCIAL STATEMENTS
        # ----------------------------------------------------

        try:
            income = ticker.financials
        except Exception:
            income = None

        try:
            balance = ticker.balance_sheet
        except Exception:
            balance = None

        try:
            cashflow = ticker.cashflow
        except Exception:
            cashflow = None

        # ----------------------------------------------------
        # REVENUE
        # ----------------------------------------------------

        revenue = get_latest_value(
            income,
            [
                "Total Revenue",
                "Operating Revenue"
            ]
        )

        # ----------------------------------------------------
        # NET INCOME
        # ----------------------------------------------------

        net_income = get_latest_value(
            income,
            [
                "Net Income",
                "Net Income Common Stockholders"
            ]
        )

        # ----------------------------------------------------
        # EBIT
        # ----------------------------------------------------

        ebit = get_latest_value(
            income,
            [
                "EBIT",
                "Operating Income"
            ]
        )

        # ----------------------------------------------------
        # TOTAL DEBT
        # ----------------------------------------------------

        total_debt = get_latest_value(
            balance,
            [
                "Total Debt"
            ]
        )

        # ----------------------------------------------------
        # EQUITY
        # ----------------------------------------------------

        equity = get_latest_value(
            balance,
            [
                "Stockholders Equity",
                "Common Stock Equity",
                "Total Equity Gross Minority Interest"
            ]
        )

        # ----------------------------------------------------
        # OPERATING CASH FLOW
        # ----------------------------------------------------

        operating_cash_flow = get_latest_value(
            cashflow,
            [
                "Operating Cash Flow",
                "Total Cash From Operating Activities"
            ]
        )

        # ----------------------------------------------------
        # FREE CASH FLOW
        # ----------------------------------------------------

        free_cash_flow = get_latest_value(
            cashflow,
            [
                "Free Cash Flow"
            ]
        )

        # ----------------------------------------------------
        # EPS
        # ----------------------------------------------------

        eps = info.get("trailingEps")

        # ----------------------------------------------------
        # REVENUE GROWTH
        # ----------------------------------------------------

        latest_revenue, previous_revenue = get_latest_two_values(
            income,
            [
                "Total Revenue",
                "Operating Revenue"
            ]
        )

        revenue_growth = calculate_growth(
            latest_revenue,
            previous_revenue
        )

        # ----------------------------------------------------
        # PROFIT GROWTH
        # ----------------------------------------------------

        latest_profit, previous_profit = get_latest_two_values(
            income,
            [
                "Net Income",
                "Net Income Common Stockholders"
            ]
        )

        profit_growth = calculate_growth(
            latest_profit,
            previous_profit
        )

        # ----------------------------------------------------
        # P/E RATIO
        # ----------------------------------------------------

        if (
            price is not None
            and eps is not None
            and eps > 0
        ):
            pe_ratio = price / eps
        else:
            pe_ratio = None

        # ----------------------------------------------------
        # ROE
        # ----------------------------------------------------

        if (
            net_income is not None
            and equity is not None
            and equity != 0
        ):
            roe = (net_income / equity) * 100
        else:
            roe = None

        # ----------------------------------------------------
        # ROCE
        # Simplified educational calculation
        # ----------------------------------------------------

        if (
            ebit is not None
            and equity is not None
            and total_debt is not None
            and (equity + total_debt) != 0
        ):
            roce = (
                ebit / (equity + total_debt)
            ) * 100
        else:
            roce = None

        # ----------------------------------------------------
        # DEBT TO EQUITY
        # ----------------------------------------------------

        if (
            total_debt is not None
            and equity is not None
            and equity != 0
        ):
            debt_to_equity = total_debt / equity
        else:
            debt_to_equity = None

        # ----------------------------------------------------
        # RETURN DATA
        # ----------------------------------------------------

        company_data = {
            "name": name,
            "price": price,
            "market_cap": market_cap,
            "sector": sector,
            "industry": industry,

            "listing_currency": listing_currency,
            "financial_currency": financial_currency,

            "price_symbol": price_symbol,
            "financial_symbol": financial_symbol,

            "revenue": revenue,
            "net_income": net_income,
            "ebit": ebit,

            "total_debt": total_debt,
            "equity": equity,

            "operating_cash_flow": operating_cash_flow,
            "free_cash_flow": free_cash_flow,

            "eps": eps,
            "pe_ratio": pe_ratio,

            "roe": roe,
            "roce": roce,
            "debt_to_equity": debt_to_equity,

            "revenue_growth": revenue_growth,
            "profit_growth": profit_growth
        }

        return company_data

    except Exception as e:

        print(f"Error retrieving company data: {e}")

        return None


# ============================================================
# HISTORICAL PRICE DATA
# ============================================================

def get_price_history(symbol, period="1y"):
    """
    Fetch historical closing prices for a stock.
    """

    try:
        ticker = yf.Ticker(symbol)

        history = ticker.history(
            period=period,
            auto_adjust=False
        )

        if history.empty:
            return None

        return history[["Close"]]

    except Exception as e:

        print(
            f"Error fetching price history: {e}"
        )

        return None