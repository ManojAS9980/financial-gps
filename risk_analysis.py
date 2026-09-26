def show_risk_analysis(company):
    """
    Display an educational risk and financial-health analysis.
    This is not an investment recommendation.
    """

    print("\n========== RISK & FINANCIAL HEALTH ==========")

    # -----------------------------------
    # Debt-to-Equity
    # -----------------------------------
    debt_to_equity = company.get("debt_to_equity")

    print("\n🏦 Leverage")

    if debt_to_equity is None:
        print("Debt-to-Equity: Not available")
    else:
        print(f"Debt-to-Equity: {debt_to_equity:.2f}")

        if debt_to_equity < 0.5:
            print(
                "Observation: Debt is relatively small compared "
                "with shareholders' equity under this measure."
            )
        elif debt_to_equity < 1:
            print(
                "Observation: Debt and equity are below a 1:1 ratio."
            )
        else:
            print(
                "Observation: Debt is at least as large as "
                "shareholders' equity under this measure."
            )

        print(
            "Context: Debt levels should be compared with "
            "companies in the same industry."
        )

    # -----------------------------------
    # Operating Cash Flow
    # -----------------------------------
    operating_cash_flow = company.get(
        "operating_cash_flow"
    )

    print("\n💵 Operating Cash Flow")

    if operating_cash_flow is None:
        print("Operating Cash Flow: Not available")
    else:
        print(
            f"Operating Cash Flow: "
            f"{company['financial_symbol']}"
            f"{operating_cash_flow:,.0f}"
        )

        if operating_cash_flow > 0:
            print(
                "Observation: The company reported positive "
                "operating cash flow in the retrieved period."
            )
        else:
            print(
                "Observation: The company reported negative "
                "operating cash flow in the retrieved period."
            )

    # -----------------------------------
    # Free Cash Flow
    # -----------------------------------
    free_cash_flow = company.get("free_cash_flow")

    print("\n💰 Free Cash Flow")

    if free_cash_flow is None:
        print("Free Cash Flow: Not available")
    else:
        print(
            f"Free Cash Flow: "
            f"{company['financial_symbol']}"
            f"{free_cash_flow:,.0f}"
        )

        if free_cash_flow > 0:
            print(
                "Observation: Free cash flow was positive "
                "in the retrieved period."
            )
        else:
            print(
                "Observation: Free cash flow was negative "
                "in the retrieved period."
            )

    # -----------------------------------
    # Profitability
    # -----------------------------------
    roe = company.get("roe")
    roce = company.get("roce")

    print("\n📈 Profitability")

    if roe is None:
        print("ROE: Not available")
    else:
        print(f"ROE: {roe:.2f}%")

    if roce is None:
        print("ROCE: Not available")
    else:
        print(f"ROCE: {roce:.2f}%")

    if roe is not None and roce is not None:
        print(
            "Observation: ROE and ROCE are profitability "
            "measures that should be evaluated together with "
            "the company's business model and industry."
        )

    # -----------------------------------
    # Growth
    # -----------------------------------
    revenue_growth = company.get("revenue_growth")
    profit_growth = company.get("profit_growth")

    print("\n📊 Growth")

    if revenue_growth is None:
        print("Revenue Growth: Not available")
    else:
        print(
            f"Revenue Growth: "
            f"{revenue_growth:.2f}%"
        )

    if profit_growth is None:
        print("Profit Growth: Not available")
    else:
        print(
            f"Profit Growth: "
            f"{profit_growth:.2f}%"
        )

    if (
        revenue_growth is not None
        and profit_growth is not None
    ):
        if revenue_growth > 0 and profit_growth > 0:
            print(
                "Observation: Both revenue and profit increased "
                "between the latest two available annual periods."
            )
        elif revenue_growth > 0 and profit_growth <= 0:
            print(
                "Observation: Revenue increased while profit "
                "did not increase between the two periods."
            )
        elif revenue_growth <= 0 and profit_growth > 0:
            print(
                "Observation: Profit increased while revenue "
                "did not increase between the two periods."
            )
        else:
            print(
                "Observation: Both revenue and profit declined "
                "between the two periods."
            )

    # -----------------------------------
    # Final note
    # -----------------------------------
    print("\n========== IMPORTANT ==========")
    print(
        "These observations are educational and use the "
        "available financial data."
    )
    print(
        "A company's financial risk should be assessed using "
        "multiple periods, industry context, accounting details, "
        "and other relevant information."
    )
    print(
        "This section does not provide a buy or sell recommendation."
    )