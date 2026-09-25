import yfinance as yf


def get_company_data(symbol):
    ticker = yf.Ticker(symbol)

    try:
        info = ticker.info

        return {
            "name": info.get("longName", "Not available"),
            "price": info.get("currentPrice", "Not available"),
            "market_cap": info.get("marketCap", "Not available"),
            "sector": info.get("sector", "Not available"),
            "industry": info.get("industry", "Not available"),
        }

    except Exception as error:
        print(f"\n❌ Could not fetch company data: {error}")
        return None