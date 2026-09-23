print("=" * 40)
print("          FINANCIAL GPS")
print("=" * 40)

print("\nWelcome to Financial GPS!")
print("Your beginner-friendly financial market guide.\n")

name = input("What is your name? ")

print(f"\nHello {name}! 👋")
print("Let's explore the financial markets.\n")
def stock_market_menu():
    def financial_metrics_menu():
     while True:
        print("\n========== FINANCIAL METRICS ==========")
        print("1. EPS (Earnings Per Share)")
        print("2. P/E Ratio")
        print("3. ROE (Return on Equity)")
        print("4. ROCE (Return on Capital Employed)")
        print("5. Debt-to-Equity")
        print("6. Revenue Growth")
        print("7. Profit Growth")
        print("8. Back to Stock Market")

        choice = input("\nChoose an option (1-8): ")

        if choice == "1":
            print("\n📊 EPS - EARNINGS PER SHARE")
            print("EPS tells us how much profit belongs to each share.")
            print("\nFormula:")
            print("EPS = Net Profit / Number of Outstanding Shares")
            print("\nExample:")
            print("Net Profit = ₹100 crore")
            print("Shares = 10 crore")
            print("EPS = ₹10 per share")

        elif choice == "2":
            print("\n💰 P/E RATIO - PRICE TO EARNINGS")
            print("P/E compares a company's share price with its earnings per share.")
            print("\nFormula:")
            print("P/E = Share Price / EPS")
            print("\nExample:")
            print("Share Price = ₹200")
            print("EPS = ₹10")
            print("P/E = 20")

        elif choice == "3":
            print("\n📈 ROE - RETURN ON EQUITY")
            print("ROE shows how efficiently a company generates profit from shareholders' equity.")
            print("\nFormula:")
            print("ROE = Net Profit / Shareholders' Equity × 100")
            print("\nExample:")
            print("Net Profit = ₹20 crore")
            print("Equity = ₹100 crore")
            print("ROE = 20%")

        elif choice == "4":
            print("\n🏭 ROCE - RETURN ON CAPITAL EMPLOYED")
            print("ROCE measures how efficiently a company uses the capital available to it.")
            print("\nA common formula is:")
            print("ROCE = EBIT / Capital Employed × 100")
            print("\nHigher ROCE can indicate more efficient use of capital.")
            print("It should be compared with companies in the same industry.")

        elif choice == "5":
            print("\n🏦 DEBT-TO-EQUITY RATIO")
            print("This compares a company's debt with shareholders' equity.")
            print("\nFormula:")
            print("Debt-to-Equity = Total Debt / Shareholders' Equity")
            print("\nExample:")
            print("Debt = ₹50 crore")
            print("Equity = ₹100 crore")
            print("Debt-to-Equity = 0.5")

        elif choice == "6":
            print("\n📈 REVENUE GROWTH")
            print("Revenue growth shows how a company's sales change over time.")
            print("\nFormula:")
            print("Growth % = (Current Revenue - Previous Revenue)")
            print("           / Previous Revenue × 100")

        elif choice == "7":
            print("\n💹 PROFIT GROWTH")
            print("Profit growth shows how a company's profit changes over time.")
            print("\nFormula:")
            print("Growth % = (Current Profit - Previous Profit)")
            print("           / Previous Profit × 100")

        elif choice == "8":
            print("\nReturning to Stock Market...")
            break

        else:
            print("\n❌ Invalid option. Please choose 1-8.")
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