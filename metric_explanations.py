def show_metric_explanations(company):
    """
    Display beginner-friendly explanations of the
    financial metrics returned for a company.
    """

    print("\n========== UNDERSTANDING THE METRICS ==========")

    # EPS
    if company["eps"] is not None:
        print("\n📊 EPS - Earnings Per Share")
        print(
            "EPS shows the earnings attributable to each "
            "outstanding share."
        )
        print(
            f"Current trailing EPS: "
            f"₹{company['eps']:,.2f}"
        )
        print(
            "Use it alongside revenue, profit growth, "
            "and other financial information."
        )

    # P/E
    if company["pe_ratio"] is not None:
        print("\n💰 P/E - Price to Earnings")
        print(
            "P/E compares the market price of a share "
            "with its earnings per share."
        )
        print(
            f"Current trailing P/E: "
            f"{company['pe_ratio']:,.2f}"
        )
        print(
            "P/E is most useful when compared with the "
            "company's history and relevant peers."
        )

    # ROE
    if company["roe"] is not None:
        print("\n📈 ROE - Return on Equity")
        print(
            "ROE measures profit generated relative to "
            "shareholders' equity."
        )
        print(
            f"Current ROE: "
            f"{company['roe']:.2f}%"
        )
        print(
            "ROE can be influenced by profitability, "
            "leverage, and changes in equity."
        )

    # ROCE
    if company["roce"] is not None:
        print("\n🏭 ROCE - Return on Capital Employed")
        print(
            "ROCE relates operating profit to the capital "
            "used by the business."
        )
        print(
            f"Current ROCE: "
            f"{company['roce']:.2f}%"
        )
        print(
            "Compare ROCE with companies in the same "
            "industry and across multiple periods."
        )

    # Debt-to-Equity
    if company["debt_to_equity"] is not None:
        print("\n🏦 Debt-to-Equity")
        print(
            "Debt-to-Equity indicates the relationship "
            "between debt and shareholders' equity."
        )
        print(
            f"Current Debt-to-Equity: "
            f"{company['debt_to_equity']:.2f}"
        )
        print(
            "It helps users understand financial leverage "
            "and should be interpreted in industry context."
        )

    # Revenue Growth
    if company["revenue_growth"] is not None:
        print("\n📈 Revenue Growth")
        print(
            "Revenue growth measures the change in a "
            "company's sales over time."
        )
        print(
            f"Latest annual growth: "
            f"{company['revenue_growth']:.2f}%"
        )
        print(
            "A single year's growth does not describe the "
            "entire long-term trend."
        )

    # Profit Growth
    if company["profit_growth"] is not None:
        print("\n💹 Profit Growth")
        print(
            "Profit growth measures how net income changes "
            "over time."
        )
        print(
            f"Latest annual growth: "
            f"{company['profit_growth']:.2f}%"
        )
        print(
            "Profit growth should be considered together "
            "with revenue, margins, and cash flow."
        )

    print("\nNote: These explanations are educational.")
    print(
        "Financial metrics should be evaluated using "
        "multiple factors and appropriate context."
    )