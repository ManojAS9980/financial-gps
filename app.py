import streamlit as st
from market_data import get_company_data, get_price_history


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Financial GPS",
    page_icon="🧭",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------

st.markdown(
    """
    <style>
    .main {
        padding-top: 1rem;
    }

    .gps-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 0;
    }

    .gps-subtitle {
        font-size: 18px;
        opacity: 0.75;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 600;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="gps-title">🧭 Financial GPS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="gps-subtitle">'
    'Beginner-friendly financial market research platform'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🔎 Company Research")

symbol = st.sidebar.text_input(
    "Enter stock symbol",
    value="TCS.NS",
    help="Example: TCS.NS, INFY.NS, RELIANCE.NS"
)

search_button = st.sidebar.button(
    "Research Company",
    use_container_width=True
)


st.sidebar.markdown("---")

st.sidebar.info(
    "Financial GPS is an educational project. "
    "It does not provide personalized investment advice."
)


# --------------------------------------------------
# LOAD COMPANY DATA
# --------------------------------------------------

if search_button or symbol:

    symbol = symbol.strip().upper()

    with st.spinner("Fetching company data..."):

        company = get_company_data(symbol)

    if company is None:

        st.error(
            "❌ Could not retrieve company data. "
            "Check the symbol and try again."
        )

        st.stop()


    # --------------------------------------------------
    # COMPANY HEADER
    # --------------------------------------------------

    st.markdown(
        f"## 🏢 {company.get('name', 'Unknown Company')}"
    )

    st.caption(
        f"Symbol: {symbol}  |  "
        f"Sector: {company.get('sector', 'N/A')}  |  "
        f"Industry: {company.get('industry', 'N/A')}"
    )


    # --------------------------------------------------
    # TOP METRICS
    # --------------------------------------------------

    price_symbol = company.get("price_symbol", "")
    financial_symbol = company.get("financial_symbol", "")

    current_price = company.get("price")
    market_cap = company.get("market_cap")
    eps = company.get("eps")
    pe = company.get("pe_ratio")


    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if current_price is not None:
            st.metric(
                "Current Price",
                f"{price_symbol}{current_price:,.2f}"
            )
        else:
            st.metric("Current Price", "N/A")

    with col2:
        if market_cap is not None:
            st.metric(
                "Market Cap",
                f"{price_symbol}{market_cap:,.0f}"
            )
        else:
            st.metric("Market Cap", "N/A")

    with col3:
        if eps is not None:
            st.metric(
                "Trailing EPS",
                f"{financial_symbol}{eps:,.2f}"
            )
        else:
            st.metric("Trailing EPS", "N/A")

    with col4:
        if pe is not None:
            st.metric(
                "Trailing P/E",
                f"{pe:,.2f}"
            )
        else:
            st.metric("Trailing P/E", "N/A")


    st.markdown("---")


    # --------------------------------------------------
    # TABS
    # --------------------------------------------------

    overview_tab, financials_tab, risk_tab = st.tabs(
        [
            "📊 Overview",
            "💰 Financials",
            "🛡️ Risk & Health"
        ]
    )


    # ==================================================
    # OVERVIEW TAB
    # ==================================================

    with overview_tab:

        st.markdown(
            '<div class="section-title">Key Financial Metrics</div>',
            unsafe_allow_html=True
        )

        metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

        with metric_col1:
            roe = company.get("roe")

            if roe is not None:
                st.metric("ROE", f"{roe:.2f}%")
            else:
                st.metric("ROE", "N/A")

        with metric_col2:
            roce = company.get("roce")

            if roce is not None:
                st.metric("ROCE", f"{roce:.2f}%")
            else:
                st.metric("ROCE", "N/A")

        with metric_col3:
            debt_equity = company.get("debt_to_equity")

            if debt_equity is not None:
                st.metric(
                    "Debt / Equity",
                    f"{debt_equity:.2f}"
                )
            else:
                st.metric("Debt / Equity", "N/A")

        with metric_col4:
            revenue_growth = company.get("revenue_growth")

            if revenue_growth is not None:
                st.metric(
                    "Revenue Growth",
                    f"{revenue_growth:.2f}%"
                )
            else:
                st.metric("Revenue Growth", "N/A")


        st.markdown("---")

        st.markdown("### 📚 What do these metrics mean?")

        st.write(
            """
            **EPS** — Earnings generated for each share.

            **P/E Ratio** — Compares a company's share price with
            its earnings per share.

            **ROE** — Shows how efficiently shareholder equity
            is being used to generate profit.

            **ROCE** — An educational measure of how efficiently
            capital is being used.

            **Debt / Equity** — Gives an indication of the
            company's debt relative to shareholder equity.

            **Revenue Growth** — Shows how revenue has changed
            between the latest reported periods.
            """
        )
            # ==================================================
    # PRICE HISTORY
    # ==================================================

    st.markdown("---")

    st.subheader("📈 Price History")

    price_history = get_price_history(symbol)

    if price_history is not None:

        st.line_chart(
            price_history["Close"],
            height=350
        )

    else:

        st.warning(
            "Historical price data could not be retrieved."
        )


    # ==================================================
    # FINANCIALS TAB
    # ==================================================

    with financials_tab:

        st.markdown(
            '<div class="section-title">Financial Overview</div>',
            unsafe_allow_html=True
        )

        financial_col1, financial_col2 = st.columns(2)

        with financial_col1:

            revenue = company.get("revenue")
            net_income = company.get("net_income")
            ebit = company.get("ebit")

            st.subheader("Income Statement")

            if revenue is not None:
                st.write(
                    f"**Revenue:** "
                    f"{financial_symbol}{revenue:,.0f}"
                )
            else:
                st.write("**Revenue:** N/A")

            if net_income is not None:
                st.write(
                    f"**Net Income:** "
                    f"{financial_symbol}{net_income:,.0f}"
                )
            else:
                st.write("**Net Income:** N/A")

            if ebit is not None:
                st.write(
                    f"**EBIT:** "
                    f"{financial_symbol}{ebit:,.0f}"
                )
            else:
                st.write("**EBIT:** N/A")


        with financial_col2:

            debt = company.get("total_debt")
            equity = company.get("equity")
            operating_cash_flow = company.get(
                "operating_cash_flow"
            )
            free_cash_flow = company.get(
                "free_cash_flow"
            )

            st.subheader("Balance Sheet & Cash Flow")

            if debt is not None:
                st.write(
                    f"**Total Debt:** "
                    f"{financial_symbol}{debt:,.0f}"
                )
            else:
                st.write("**Total Debt:** N/A")

            if equity is not None:
                st.write(
                    f"**Equity:** "
                    f"{financial_symbol}{equity:,.0f}"
                )
            else:
                st.write("**Equity:** N/A")

            if operating_cash_flow is not None:
                st.write(
                    f"**Operating Cash Flow:** "
                    f"{financial_symbol}{operating_cash_flow:,.0f}"
                )
            else:
                st.write("**Operating Cash Flow:** N/A")

            if free_cash_flow is not None:
                st.write(
                    f"**Free Cash Flow:** "
                    f"{financial_symbol}{free_cash_flow:,.0f}"
                )
            else:
                st.write("**Free Cash Flow:** N/A")


        st.markdown("---")

        st.subheader("Growth")

        growth_col1, growth_col2 = st.columns(2)

        with growth_col1:

            revenue_growth = company.get("revenue_growth")

            if revenue_growth is not None:
                st.metric(
                    "Revenue Growth",
                    f"{revenue_growth:.2f}%"
                )
            else:
                st.metric("Revenue Growth", "N/A")

        with growth_col2:

            profit_growth = company.get("profit_growth")

            if profit_growth is not None:
                st.metric(
                    "Profit Growth",
                    f"{profit_growth:.2f}%"
                )
            else:
                st.metric("Profit Growth", "N/A")


    # ==================================================
    # RISK TAB
    # ==================================================

    with risk_tab:

        st.markdown(
            '<div class="section-title">'
            'Risk & Financial Health'
            '</div>',
            unsafe_allow_html=True
        )

        st.info(
            "This section provides educational observations "
            "from financial data. It is not a buy/sell signal."
        )


        debt_equity = company.get("debt_to_equity")
        operating_cash_flow = company.get(
            "operating_cash_flow"
        )
        free_cash_flow = company.get(
            "free_cash_flow"
        )
        roe = company.get("roe")
        roce = company.get("roce")


        st.subheader("Capital Structure")

        if debt_equity is not None:

            st.write(
                f"**Debt-to-Equity:** "
                f"{debt_equity:.2f}"
            )

            if debt_equity < 1:
                st.success(
                    "Debt is lower than equity based on "
                    "the calculated ratio."
                )
            else:
                st.warning(
                    "Debt is at least as large as equity "
                    "based on the calculated ratio."
                )

        else:
            st.write("Debt-to-Equity data unavailable.")


        st.subheader("Cash Flow")

        if operating_cash_flow is not None:

            st.write(
                f"**Operating Cash Flow:** "
                f"{financial_symbol}{operating_cash_flow:,.0f}"
            )

        else:
            st.write("Operating Cash Flow: N/A")


        if free_cash_flow is not None:

            st.write(
                f"**Free Cash Flow:** "
                f"{financial_symbol}{free_cash_flow:,.0f}"
            )

        else:
            st.write("Free Cash Flow: N/A")


        st.subheader("Returns")

        return_col1, return_col2 = st.columns(2)

        with return_col1:

            if roe is not None:
                st.metric("ROE", f"{roe:.2f}%")
            else:
                st.metric("ROE", "N/A")

        with return_col2:

            if roce is not None:
                st.metric("ROCE", f"{roce:.2f}%")
            else:
                st.metric("ROCE", "N/A")


        st.markdown("---")

        st.caption(
            "Financial GPS uses publicly available market data "
            "for educational analysis."
        )


# --------------------------------------------------
# DEFAULT MESSAGE
# --------------------------------------------------

else:

    st.info(
        "👈 Enter a company symbol in the sidebar "
        "to begin your research."
    )