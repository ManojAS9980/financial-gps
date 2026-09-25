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
            print("EPS = Net Profit / Number of Outstanding Shares")

            try:
                net_profit = float(input("\nEnter net profit: ₹"))
                shares = float(input("Enter number of outstanding shares: "))

                if shares <= 0:
                    print("\n❌ Number of shares must be greater than zero.")
                else:
                    eps = net_profit / shares

                    print(f"\nNet Profit: ₹{net_profit:,.2f}")
                    print(f"Shares: {shares:,.2f}")
                    print(f"EPS: ₹{eps:,.2f}")

            except ValueError:
                print("\n❌ Please enter numbers only.")

        elif choice == "2":
            print("\n💰 P/E RATIO - PRICE TO EARNINGS")

            try:
                share_price = float(input("\nEnter share price: ₹"))
                eps = float(input("Enter EPS: ₹"))

                if eps <= 0:
                    print("\n❌ EPS must be greater than zero.")
                else:
                    pe_ratio = share_price / eps

                    print(f"\nShare Price: ₹{share_price:,.2f}")
                    print(f"EPS: ₹{eps:,.2f}")
                    print(f"P/E Ratio: {pe_ratio:,.2f}")

            except ValueError:
                print("\n❌ Please enter numbers only.")

        elif choice == "3":
            print("\n📈 ROE - RETURN ON EQUITY")

            try:
                net_profit = float(input("\nEnter net profit: ₹"))
                equity = float(input("Enter shareholders' equity: ₹"))

                if equity <= 0:
                    print("\n❌ Equity must be greater than zero.")
                else:
                    roe = (net_profit / equity) * 100

                    print(f"\nNet Profit: ₹{net_profit:,.2f}")
                    print(f"Equity: ₹{equity:,.2f}")
                    print(f"ROE: {roe:,.2f}%")

            except ValueError:
                print("\n❌ Please enter numbers only.")

        elif choice == "4":
            print("\n🏭 ROCE - RETURN ON CAPITAL EMPLOYED")

            try:
                ebit = float(input("\nEnter EBIT: ₹"))
                capital_employed = float(
                    input("Enter capital employed: ₹")
                )

                if capital_employed <= 0:
                    print("\n❌ Capital employed must be greater than zero.")
                else:
                    roce = (ebit / capital_employed) * 100

                    print(f"\nEBIT: ₹{ebit:,.2f}")
                    print(f"Capital Employed: ₹{capital_employed:,.2f}")
                    print(f"ROCE: {roce:,.2f}%")

            except ValueError:
                print("\n❌ Please enter numbers only.")

        elif choice == "5":
            print("\n🏦 DEBT-TO-EQUITY RATIO")

            try:
                debt = float(input("\nEnter total debt: ₹"))
                equity = float(input("Enter shareholders' equity: ₹"))

                if equity <= 0:
                    print("\n❌ Equity must be greater than zero.")
                else:
                    debt_to_equity = debt / equity

                    print(f"\nDebt: ₹{debt:,.2f}")
                    print(f"Equity: ₹{equity:,.2f}")
                    print(f"Debt-to-Equity: {debt_to_equity:,.2f}")

            except ValueError:
                print("\n❌ Please enter numbers only.")

        elif choice == "6":
            print("\n📈 REVENUE GROWTH")

            try:
                previous_revenue = float(
                    input("\nEnter previous revenue: ₹")
                )
                current_revenue = float(
                    input("Enter current revenue: ₹")
                )

                if previous_revenue == 0:
                    print("\n❌ Previous revenue cannot be zero.")
                else:
                    growth = (
                        (current_revenue - previous_revenue)
                        / previous_revenue
                    ) * 100

                    print(f"\nPrevious Revenue: ₹{previous_revenue:,.2f}")
                    print(f"Current Revenue: ₹{current_revenue:,.2f}")
                    print(f"Revenue Growth: {growth:,.2f}%")

            except ValueError:
                print("\n❌ Please enter numbers only.")

        elif choice == "7":
            print("\n💹 PROFIT GROWTH")

            try:
                previous_profit = float(
                    input("\nEnter previous profit: ₹")
                )
                current_profit = float(
                    input("Enter current profit: ₹")
                )

                if previous_profit == 0:
                    print("\n❌ Previous profit cannot be zero.")
                else:
                    growth = (
                        (current_profit - previous_profit)
                        / previous_profit
                    ) * 100

                    print(f"\nPrevious Profit: ₹{previous_profit:,.2f}")
                    print(f"Current Profit: ₹{current_profit:,.2f}")
                    print(f"Profit Growth: {growth:,.2f}%")

            except ValueError:
                print("\n❌ Please enter numbers only.")

        elif choice == "8":
            print("\nReturning to Stock Market...")
            break

        else:
            print("\n❌ Invalid option. Please choose 1-8.")