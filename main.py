print("=" * 40)
print("          FINANCIAL GPS")
print("=" * 40)

print("\nWelcome to Financial GPS!")
print("Your beginner-friendly financial market guide.\n")

name = input("What is your name? ")

print(f"\nHello {name}! 👋")
print("Let's explore the financial markets.\n")

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
        print("\n📈 STOCK MARKET")
        print("Learn how stocks work and how to research companies.")

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