print("=" * 40)
print("          FINANCIAL GPS")
print("=" * 40)

print("\nWelcome to Financial GPS!")
print("Your beginner-friendly financial market guide.\n")

name = input("What is your name? ")

print(f"\nHello {name}! 👋")
print("Let's explore the financial markets.\n")
def stock_market_menu():
    while True:
        print("\n========== STOCK MARKET ==========")
        print("1. What is a Stock?")
        print("2. How to Analyze a Company")
        print("3. Financial Metrics")
        print("4. Valuation Basics")
        print("5. Compare Companies")
        print("6. Back to Main Menu")

        choice = input("\nChoose an option (1-6): ")

        if choice == "1":
            print("\n📈 WHAT IS A STOCK?")
            print("A stock represents ownership in a company.")
            print("When you buy a stock, you own a small part of that company.")

        elif choice == "2":
            print("\n🔎 HOW TO ANALYZE A COMPANY")
            print("We will later analyze:")
            print("- Business model")
            print("- Revenue and profit")
            print("- Debt")
            print("- Cash flow")
            print("- Growth")
            print("- Competitive position")

        elif choice == "3":
            print("\n📊 FINANCIAL METRICS")
            print("We will learn about:")
            print("- EPS")
            print("- ROE")
            print("- ROCE")
            print("- Debt-to-Equity")
            print("- Revenue growth")
            print("- Profit growth")

        elif choice == "4":
            print("\n💰 VALUATION BASICS")
            print("We will learn about:")
            print("- P/E Ratio")
            print("- P/B Ratio")
            print("- EV/EBITDA")
            print("- PEG Ratio")

        elif choice == "5":
            print("\n⚖️ COMPARE COMPANIES")
            print("Company comparison will be added in a future version.")

        elif choice == "6":
            print("\nReturning to Main Menu...")
            break

        else:
            print("\n❌ Invalid option. Please choose 1-6.")
while True:
    print("\n========== MAIN MENU ==========")
    print("1. Stock Market")
    print("2. ETFs")
    print("3. Mutual Funds")
    print("4. Cryptocurrency")
    print("5. Risk Management")
    print("6. Exit")

    choice = input("\nChoose an option (1-6): ")

    if choice == "1":
        stock_market_menu() 
    elif choice == "2":
        print("\n📊 ETFs")
        print("Learn about Exchange Traded Funds and diversification.")

    elif choice == "3":
        print("\n💰 MUTUAL FUNDS")
        print("Learn about mutual funds, NAV, returns and risk.")

    elif choice == "4":
        print("\n₿ CRYPTOCURRENCY")
        print("Learn about cryptocurrencies and blockchain.")

    elif choice == "5":
        print("\n⚠️ RISK MANAGEMENT")
        print("Learn about risk, diversification and position sizing.")

    elif choice == "6":
        print("\nThank you for using Financial GPS! 🚀")
        break

    else:
        print("\n❌ Invalid option. Please choose 1-6.")