from financial_metrics import financial_metrics_menu
from market_data import get_company_data


def stock_market_menu():
    while True:
        print("\n========== STOCK MARKET ==========")
        print("1. What is a Stock?")
        print("2. Company Research")
        print("3. Financial Metrics")
        print("4. Valuation Basics")
        print("5. Compare Companies")
        print("6. Back to Main Menu")

        choice = input("\nChoose an option (1-6): ").strip()

        if choice == "1":
            print("\n📈 WHAT IS A STOCK?")
            print("A stock represents ownership in a company.")
            print("When you buy a stock, you own a small part of that company.")

        elif choice == "2":
            print("\n🔎 COMPANY RESEARCH")

            symbol = input(
                "Enter stock symbol (example: TCS.NS): "
            ).strip().upper()

            if not symbol:
                print("\n❌ Please enter a stock symbol.")

            else:
                company = get_company_data(symbol)

                if company:
                    print("\n========== COMPANY SNAPSHOT ==========")

                    print(f"Company: {company['name']}")
                    print(f"Sector: {company['sector']}")
                    print(f"Industry: {company['industry']}")

                    print("\n---------- Market Data ----------")
                    print(f"Current Price: {company['price']}")
                    print(f"Market Cap: {company['market_cap']}")

                    print("\n---------- Financial Data ----------")
                    print(f"Revenue: {company['revenue']}")
                    print(f"Net Income: {company['net_income']}")
                    print(f"EBIT: {company['ebit']}")
                    print(f"Total Debt: {company['total_debt']}")
                    print(
                        f"Shareholders' Equity: "
                        f"{company['equity']}"
                    )
                    print(
                        f"Operating Cash Flow: "
                        f"{company['operating_cash_flow']}"
                    )
                    print(
                        f"Free Cash Flow: "
                        f"{company['free_cash_flow']}"
                    )

                    print("\n---------- Calculated Ratios ----------")

                    if company["roe"] is not None:
                        print(f"ROE: {company['roe']:.2f}%")
                    else:
                        print("ROE: Not available")

                    if company["roce"] is not None:
                        print(f"ROCE: {company['roce']:.2f}%")
                    else:
                        print("ROCE: Not available")

                    if company["debt_to_equity"] is not None:
                        print(
                            f"Debt-to-Equity: "
                            f"{company['debt_to_equity']:.2f}"
                        )
                    else:
                        print("Debt-to-Equity: Not available")

                else:
                    print("\n❌ Could not retrieve company data.")

        elif choice == "3":
            financial_metrics_menu()

        elif choice == "4":
            print("\n💰 VALUATION BASICS")
            print("We will learn about:")
            print("- P/E Ratio")
            print("- P/B Ratio")
            print("- EV/EBITDA")
            print("- PEG Ratio")

        elif choice == "5":
            print("\n⚖️ COMPARE COMPANIES")
            print(
                "Company comparison will be added "
                "in a future version."
            )

        elif choice == "6":
            print("\nReturning to Main Menu...")
            break

        else:
            print("\n❌ Invalid option. Please choose 1-6.")