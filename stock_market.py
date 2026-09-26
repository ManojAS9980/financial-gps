from financial_metrics import financial_metrics_menu
from market_data import get_company_data
from metric_explanations import show_metric_explanations


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
            print(
                "When you buy a stock, you own a small part "
                "of that company."
            )

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
                    print(
                        "\n========== COMPANY SNAPSHOT =========="
                    )

                    print(f"Company: {company['name']}")
                    print(f"Sector: {company['sector']}")
                    print(f"Industry: {company['industry']}")

                    print("\n---------- Market Data ----------")

                    if company["price"] is not None:
                        print(
                            f"Current Price: "
                            f"₹{company['price']:,.2f}"
                        )
                    else:
                        print("Current Price: Not available")

                    if company["market_cap"] is not None:
                        print(
                            f"Market Cap: "
                            f"₹{company['market_cap']:,.0f}"
                        )
                    else:
                        print("Market Cap: Not available")

                    print("\n---------- Financial Data ----------")

                    if company["revenue"] is not None:
                        print(
                            f"Revenue: "
                            f"₹{company['revenue']:,.0f}"
                        )
                    else:
                        print("Revenue: Not available")

                    if company["net_income"] is not None:
                        print(
                            f"Net Income: "
                            f"₹{company['net_income']:,.0f}"
                        )
                    else:
                        print("Net Income: Not available")

                    if company["ebit"] is not None:
                        print(
                            f"EBIT: "
                            f"₹{company['ebit']:,.0f}"
                        )
                    else:
                        print("EBIT: Not available")

                    if company["total_debt"] is not None:
                        print(
                            f"Total Debt: "
                            f"₹{company['total_debt']:,.0f}"
                        )
                    else:
                        print("Total Debt: Not available")

                    if company["equity"] is not None:
                        print(
                            f"Shareholders' Equity: "
                            f"₹{company['equity']:,.0f}"
                        )
                    else:
                        print(
                            "Shareholders' Equity: Not available"
                        )

                    if company["operating_cash_flow"] is not None:
                        print(
                            f"Operating Cash Flow: "
                            f"₹{company['operating_cash_flow']:,.0f}"
                        )
                    else:
                        print(
                            "Operating Cash Flow: Not available"
                        )

                    if company["free_cash_flow"] is not None:
                        print(
                            f"Free Cash Flow: "
                            f"₹{company['free_cash_flow']:,.0f}"
                        )
                    else:
                        print(
                            "Free Cash Flow: Not available"
                        )

                    print(
                        "\n---------- Valuation & Ratios ----------"
                    )

                    if company["eps"] is not None:
                        print(
                            f"Trailing EPS: "
                            f"₹{company['eps']:,.2f}"
                        )
                    else:
                        print("Trailing EPS: Not available")

                    if company["pe_ratio"] is not None:
                        print(
                            f"Trailing P/E: "
                            f"{company['pe_ratio']:,.2f}"
                        )
                    else:
                        print("Trailing P/E: Not available")

                    if company["roe"] is not None:
                        print(
                            f"ROE: "
                            f"{company['roe']:.2f}%"
                        )
                    else:
                        print("ROE: Not available")

                    if company["roce"] is not None:
                        print(
                            f"ROCE: "
                            f"{company['roce']:.2f}%"
                        )
                    else:
                        print("ROCE: Not available")

                    if company["debt_to_equity"] is not None:
                        print(
                            f"Debt-to-Equity: "
                            f"{company['debt_to_equity']:.2f}"
                        )
                    else:
                        print(
                            "Debt-to-Equity: Not available"
                        )

                    print("\n---------- Growth ----------")

                    if company["revenue_growth"] is not None:
                        print(
                            f"Revenue Growth: "
                            f"{company['revenue_growth']:.2f}%"
                        )
                    else:
                        print(
                            "Revenue Growth: Not available"
                        )

                    if company["profit_growth"] is not None:
                        print(
                            f"Profit Growth: "
                            f"{company['profit_growth']:.2f}%"
                        )
                    else:
                        print(
                            "Profit Growth: Not available"
                        )

                    # Beginner-friendly explanations
                    show_metric_explanations(company)

                else:
                    print(
                        "\n❌ Could not retrieve company data."
                    )

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
            print(
                "\n❌ Invalid option. Please choose 1-6."
            )