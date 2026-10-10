import streamlit as st
import pandas as pd

from market_data import (
    get_company_data,
    get_price_history,
    get_historical_financials
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def format_large_number(value, currency_symbol=""):
    """
    Convert large numbers into a compact readable format.
    """

    if value is None:
        return "N/A"

    if abs(value) >= 1_000_000_000_000:
        return f"{currency_symbol}{value / 1_000_000_000_000:.2f}T"

    if abs(value) >= 1_000_000_000:
        return f"{currency_symbol}{value / 1_000_000_000:.2f}B"

    if abs(value) >= 1_000_000:
        return f"{currency_symbol}{value / 1_000_000:.2f}M"

    if abs(value) >= 1_000:
        return f"{currency_symbol}{value / 1_000:.2f}K"

    return f"{currency_symbol}{value:,.2f}"
def comparison_value(
    data,
    key,
    currency_key=None,
    decimals=2,
    suffix=""
):
    """Format a financial metric for the comparison table."""

    value = data.get(key)

    if value is None:
        return "N/A"

    prefix = ""

    if currency_key:
        prefix = data.get(currency_key, "")

    return f"{prefix}{value:,.{decimals}f}{suffix}"


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Financial GPS",
    page_icon="🧭",
    layout="wide"
)


# ============================================================
# CUSTOM STYLING
# ============================================================

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    .gps-title {
        font-size: 46px;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 0;
    }

    .gps-subtitle {
        font-size: 18px;
        opacity: 0.70;
        margin-top: 4px;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 26px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 15px;
    }

    div[data-testid="stMetric"] {
        background: linear-gradient(
            145deg,
            rgba(40, 40, 55, 0.95),
            rgba(20, 20, 30, 0.95)
        );

        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;

        padding: 18px 20px;
        min-height: 125px;

        box-shadow:
            0 8px 24px rgba(0, 0, 0, 0.25);

        transition:
            transform 0.2s ease,
            border-color 0.2s ease;
    }

    div[data-testid="stMetric"]:hover {
        transform: translateY(-3px);
        border-color: rgba(120, 180, 255, 0.35);
    }

    div[data-testid="stMetricLabel"] {
        font-size: 14px;
        font-weight: 600;
        opacity: 0.70;
    }

    div[data-testid="stMetricValue"] {
        font-size: 30px;
        font-weight: 750;
    }

    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        min-height: 44px;
    }

    div[data-baseweb="input"] {
        border-radius: 10px;
    }

    div[data-testid="stDataFrame"] {
        border-radius: 12px;
        overflow: hidden;
    }

    div[data-testid="stAlert"] {
        border-radius: 12px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

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


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🔎 Company Research")

symbol = st.sidebar.text_input(
    "Enter stock symbol",
    value="TCS.NS",
    help="Examples: TCS.NS, INFY.NS, RELIANCE.NS"
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


# ============================================================
# COMPANY DATA
# ============================================================

symbol = symbol.strip().upper()

with st.spinner("Fetching company data..."):
    company = get_company_data(symbol)


if company is None:

    st.error(
        "❌ Could not retrieve company data. "
        "Check the stock symbol and try again."
    )

    st.stop()


# ============================================================
# COMPANY HEADER
# ============================================================

company_name = company.get("name", "Unknown Company")
sector = company.get("sector", "N/A")
industry = company.get("industry", "N/A")

st.markdown(
    f"""<div style="padding:10px 0 20px 0;">
<div style="font-size:34px;font-weight:800;letter-spacing:-0.5px;">
🏢 {company_name}
</div>
<div style="font-size:15px;opacity:0.65;margin-top:6px;">
{symbol} &nbsp;•&nbsp; {sector} &nbsp;•&nbsp; {industry}
</div>
</div>""",
    unsafe_allow_html=True
)


# ============================================================
# TOP METRICS
# ============================================================

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

        st.metric(
            "Current Price",
            "N/A"
        )


with col2:

    st.metric(
        "Market Cap",
        format_large_number(
            market_cap,
            price_symbol
        )
    )


with col3:

    if eps is not None:

        st.metric(
            "Trailing EPS",
             f"{price_symbol}{eps:,.2f}"
        
        )

    else:

        st.metric(
            "Trailing EPS",
            "N/A"
        )


with col4:

    if pe is not None:

        st.metric(
            "Trailing P/E",
            f"{pe:.2f}"
        )

    else:

        st.metric(
            "Trailing P/E",
            "N/A"
        )


st.markdown("---")


# ============================================================
# TABS
# ============================================================

overview_tab, financials_tab, risk_tab, compare_tab = st.tabs(
    [
        "📊 Overview",
        "💰 Financials",
        "🛡️ Risk & Health",
        "⚖️ Compare"
    ]
)


# ============================================================
# OVERVIEW TAB
# ============================================================

with overview_tab:

    st.markdown(
        '<div class="section-title">'
        'Key Financial Metrics'
        '</div>',
        unsafe_allow_html=True
    )

    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)


    with metric_col1:

        roe = company.get("roe")

        if roe is not None:

            st.metric(
                "ROE",
                f"{roe:.2f}%"
            )

        else:

            st.metric(
                "ROE",
                "N/A"
            )


    with metric_col2:

        roce = company.get("roce")

        if roce is not None:

            st.metric(
                "ROCE",
                f"{roce:.2f}%"
            )

        else:

            st.metric(
                "ROCE",
                "N/A"
            )


    with metric_col3:

        debt_equity = company.get("debt_to_equity")

        if debt_equity is not None:

            st.metric(
                "Debt / Equity",
                f"{debt_equity:.2f}"
            )

        else:

            st.metric(
                "Debt / Equity",
                "N/A"
            )


    with metric_col4:

        revenue_growth = company.get("revenue_growth")

        if revenue_growth is not None:

            st.metric(
                "Revenue Growth",
                f"{revenue_growth:.2f}%"
            )

        else:

            st.metric(
                "Revenue Growth",
                "N/A"
            )


    # ========================================================
    # METRIC EXPLANATIONS
    # ========================================================

    st.markdown("---")

    st.markdown(
        "### 📚 What do these metrics mean?"
    )

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


    # ========================================================
    # PRICE HISTORY
    # ========================================================

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


    # ========================================================
    # HISTORICAL FINANCIAL PERFORMANCE
    # ========================================================

    st.markdown("---")

    st.subheader(
        "📊 Historical Financial Performance"
    )

    historical_financials = get_historical_financials(symbol)

    if historical_financials is not None:

        chart_col1, chart_col2, chart_col3 = st.columns(3)


        with chart_col1:

            st.markdown("### Revenue")

            if "Revenue" in historical_financials.columns:

                st.line_chart(
                    historical_financials["Revenue"],
                    height=300
                )

            else:

                st.info(
                    "Revenue data unavailable."
                )


        with chart_col2:

            st.markdown("### Net Income")

            if "Net Income" in historical_financials.columns:

                st.line_chart(
                    historical_financials["Net Income"],
                    height=300
                )

            else:

                st.info(
                    "Net Income data unavailable."
                )


        with chart_col3:

            st.markdown("### EBIT")

            if "EBIT" in historical_financials.columns:

                st.line_chart(
                    historical_financials["EBIT"],
                    height=300
                )

            else:

                st.info(
                    "EBIT data unavailable."
                )


        st.markdown(
            "### 📋 Historical Financial Data"
        )

        st.dataframe(
            historical_financials,
            use_container_width=True
        )

    else:

        st.warning(
            "Historical financial data could not be retrieved."
        )


# ============================================================
# FINANCIALS TAB
# ============================================================

with financials_tab:

    st.markdown(
        '<div class="section-title">'
        'Financial Overview'
        '</div>',
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

            st.write(
                "**Revenue:** N/A"
            )


        if net_income is not None:

            st.write(
                f"**Net Income:** "
                f"{financial_symbol}{net_income:,.0f}"
            )

        else:

            st.write(
                "**Net Income:** N/A"
            )


        if ebit is not None:

            st.write(
                f"**EBIT:** "
                f"{financial_symbol}{ebit:,.0f}"
            )

        else:

            st.write(
                "**EBIT:** N/A"
            )


    with financial_col2:

        debt = company.get("total_debt")
        equity = company.get("equity")
        operating_cash_flow = company.get(
            "operating_cash_flow"
        )
        free_cash_flow = company.get(
            "free_cash_flow"
        )

        st.subheader(
            "Balance Sheet & Cash Flow"
        )


        if debt is not None:

            st.write(
                f"**Total Debt:** "
                f"{financial_symbol}{debt:,.0f}"
            )

        else:

            st.write(
                "**Total Debt:** N/A"
            )


        if equity is not None:

            st.write(
                f"**Equity:** "
                f"{financial_symbol}{equity:,.0f}"
            )

        else:

            st.write(
                "**Equity:** N/A"
            )


        if operating_cash_flow is not None:

            st.write(
                f"**Operating Cash Flow:** "
                f"{financial_symbol}"
                f"{operating_cash_flow:,.0f}"
            )

        else:

            st.write(
                "**Operating Cash Flow:** N/A"
            )


        if free_cash_flow is not None:

            st.write(
                f"**Free Cash Flow:** "
                f"{financial_symbol}"
                f"{free_cash_flow:,.0f}"
            )

        else:

            st.write(
                "**Free Cash Flow:** N/A"
            )


    st.markdown("---")

    st.subheader("Growth")

    growth_col1, growth_col2 = st.columns(2)


    with growth_col1:

        revenue_growth = company.get(
            "revenue_growth"
        )

        if revenue_growth is not None:

            st.metric(
                "Revenue Growth",
                f"{revenue_growth:.2f}%"
            )

        else:

            st.metric(
                "Revenue Growth",
                "N/A"
            )


    with growth_col2:

        profit_growth = company.get(
            "profit_growth"
        )

        if profit_growth is not None:

            st.metric(
                "Profit Growth",
                f"{profit_growth:.2f}%"
            )

        else:

            st.metric(
                "Profit Growth",
                "N/A"
            )


# ============================================================
# RISK & FINANCIAL HEALTH TAB
# ============================================================

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


    debt_equity = company.get(
        "debt_to_equity"
    )

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

        st.write(
            "Debt-to-Equity data unavailable."
        )


    st.subheader("Cash Flow")


    if operating_cash_flow is not None:

        st.write(
            f"**Operating Cash Flow:** "
            f"{financial_symbol}"
            f"{operating_cash_flow:,.0f}"
        )

    else:

        st.write(
            "Operating Cash Flow: N/A"
        )


    if free_cash_flow is not None:

        st.write(
            f"**Free Cash Flow:** "
            f"{financial_symbol}"
            f"{free_cash_flow:,.0f}"
        )

    else:

        st.write(
            "Free Cash Flow: N/A"
        )


    st.subheader("Returns")

    return_col1, return_col2 = st.columns(2)


    with return_col1:

        if roe is not None:

            st.metric(
                "ROE",
                f"{roe:.2f}%"
            )

        else:

            st.metric(
                "ROE",
                "N/A"
            )


    with return_col2:

        if roce is not None:

            st.metric(
                "ROCE",
                f"{roce:.2f}%"
            )

        else:

            st.metric(
                "ROCE",
                "N/A"
            )


    st.markdown("---")

    st.caption(
        "Financial GPS uses publicly available market data "
        "for educational analysis."
    )

# ============================================================
# COMPANY COMPARISON TAB
# ============================================================

with compare_tab:

    st.markdown(
        '<div class="section-title">'
        '⚖️ Company Comparison'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Compare two companies using financial and market data."
    )

    st.caption(
        "Enter two stock symbols to compare their reported metrics."
    )

    # --------------------------------------------------------
    # COMPANY INPUTS
    # --------------------------------------------------------

    compare_col1, compare_col2 = st.columns(2)

    with compare_col1:

        symbol_1 = st.text_input(
            "First Company",
            value="TCS.NS",
            key="compare_symbol_1"
        ).strip().upper()

    with compare_col2:

        symbol_2 = st.text_input(
            "Second Company",
            value="INFY.NS",
            key="compare_symbol_2"
        ).strip().upper()

    compare_button = st.button(
        "⚖️ Compare Companies",
        use_container_width=True
    )

    # --------------------------------------------------------
    # FETCH COMPANY DATA
    # --------------------------------------------------------

    if compare_button:

        if not symbol_1 or not symbol_2:

            st.error("Please enter both company symbols.")

        elif symbol_1 == symbol_2:

            st.warning(
                "Enter two different symbols to compare companies."
            )

        else:

            with st.spinner("Fetching company data..."):

                company_1 = get_company_data(symbol_1)
                company_2 = get_company_data(symbol_2)

            if company_1 is None or company_2 is None:

                st.error(
                    "Could not retrieve data for one or both companies. "
                    "Check the symbols and try again."
                )

            else:

                name_1 = company_1.get("name", symbol_1)
                name_2 = company_2.get("name", symbol_2)

                st.markdown("---")

                st.subheader("📊 Comparison Results")

                # ------------------------------------------------
                # FORMATTING HELPER
                # ------------------------------------------------

                def comparison_value(
                    data,
                    key,
                    currency_key=None,
                    decimals=2,
                    suffix=""
                ):

                    value = data.get(key)

                    if value is None:

                        return "N/A"

                    prefix = ""

                    if currency_key:

                        prefix = data.get(currency_key, "")

                    return (
                        f"{prefix}{value:,.{decimals}f}{suffix}"
                    )

                # ------------------------------------------------
                # MARKET DATA
                # ------------------------------------------------

                st.markdown("### 💹 Market Data")

                market_rows = [
                    [
                        "Current Price",
                        comparison_value(
                            company_1,
                            "price",
                            "price_symbol"
                        ),
                        comparison_value(
                            company_2,
                            "price",
                            "price_symbol"
                        )
                    ],
                    [
                        "Market Cap",
                        format_large_number(
                            company_1.get("market_cap"),
                            company_1.get("price_symbol", "")
                        ),
                        format_large_number(
                            company_2.get("market_cap"),
                            company_2.get("price_symbol", "")
                        )
                    ],
                    [
                      "Trailing EPS",
                       comparison_value(company_1, "eps", "price_symbol"),
                       comparison_value(company_2, "eps", "price_symbol")                           
                    ],
                    [
                        "Trailing P/E",
                        comparison_value(
                            company_1,
                            "pe_ratio"
                        ),
                        comparison_value(
                            company_2,
                            "pe_ratio"
                        )
                    ]
                ]

                market_df = pd.DataFrame(
                    market_rows,
                    columns=[
                        "Metric",
                        name_1,
                        name_2
                    ]
                )

                st.dataframe(
                    market_df,
                    use_container_width=True,
                    hide_index=True
                )
                # ------------------------------------------------


                # ------------------------------------------------
                # FINANCIAL METRICS
                # ------------------------------------------------

            st.markdown("### 📈 Financial Metrics")

            financial_metric_rows = [
                                [
                                    "Return on Equity (ROE)",
                                    comparison_value(
                                        company_1,
                                        "roe",
                                        suffix="%"
                                    ),
                                    comparison_value(
                                        company_2,
                                        "roe",
                                        suffix="%"
                                    )
                                ],
                                [
                                    "Return on Capital Employed (ROCE)",
                                    comparison_value(
                                        company_1,
                                        "roce",
                                        suffix="%"
                                    ),
                                    comparison_value(
                                        company_2,
                                        "roce",
                                        suffix="%"
                                    )
                                ],
                                [
                                    "Debt / Equity",
                                    comparison_value(
                                        company_1,
                                        "debt_to_equity"
                                    ),
                                    comparison_value(
                                        company_2,
                                        "debt_to_equity"
                                    )
                                ],
                                [
                                    "Revenue Growth",
                                    comparison_value(
                                        company_1,
                                        "revenue_growth",
                                        suffix="%"
                                    ),
                                    comparison_value(
                                        company_2,
                                        "revenue_growth",
                                        suffix="%"
                                    )
                                ],
                                [
                                    "Profit Growth",
                                    comparison_value(
                                        company_1,
                                        "profit_growth",
                                        suffix="%"
                                    ),
                                    comparison_value(
                                        company_2,
                                        "profit_growth",
                                        suffix="%"
                                    )
                                ]
                            ]

            metrics_df = pd.DataFrame(
                                financial_metric_rows,
                                columns=[
                                    "Metric",
                                    name_1,
                                    name_2
                                ]
                            )

            st.dataframe(
                                metrics_df,
                                use_container_width=True,
                                hide_index=True
                            )

                            # ------------------------------------------------
                            # FINANCIAL POSITION
                            # ------------------------------------------------

            st.markdown("### 💰 Financial Position")

            position_rows = [
                                [
                                    "Revenue",
                                    comparison_value(
                                        company_1,
                                        "revenue",
                                        "financial_symbol",
                                        decimals=0
                                    ),
                                    comparison_value(
                                        company_2,
                                        "revenue",
                                        "financial_symbol",
                                        decimals=0
                                    )
                                ],
                                [
                                    "Net Income",
                                    comparison_value(
                                        company_1,
                                        "net_income",
                                        "financial_symbol",
                                        decimals=0
                                    ),
                                    comparison_value(
                                        company_2,
                                        "net_income",
                                        "financial_symbol",
                                        decimals=0
                                    )
                                ],
                                [
                                    "Total Debt",
                                    comparison_value(
                                        company_1,
                                        "total_debt",
                                        "financial_symbol",
                                        decimals=0
                                    ),
                                    comparison_value(
                                        company_2,
                                        "total_debt",
                                        "financial_symbol",
                                        decimals=0
                                    )
                                ],
                                [
                                    "Equity",
                                    comparison_value(
                                        company_1,
                                        "equity",
                                        "financial_symbol",
                                        decimals=0
                                    ),
                                    comparison_value(
                                        company_2,
                                        "equity",
                                        "financial_symbol",
                                        decimals=0
                                    )
                                ]
                            ]

            position_df = pd.DataFrame(
                                position_rows,
                                columns=[
                                    "Metric",
                                    name_1,
                                    name_2
                                ]
                            )

            st.dataframe(
                                position_df,
                                use_container_width=True,
                                hide_index=True
                            )
                        # VISUAL METRIC COMPARISON

            st.markdown("### 📊 Visual Metric Comparison")

            st.caption(
                            "Compare profitability and growth metrics side by side."
                        )

            chart_data = pd.DataFrame({
                            "Metric": [
                                "ROE",
                                "ROCE",
                                "Revenue Growth",
                                "Profit Growth"
                            ],
                            name_1: [
                                company_1.get("roe"),
                                company_1.get("roce"),
                                company_1.get("revenue_growth"),
                                company_1.get("profit_growth")
                            ],
                            name_2: [
                                company_2.get("roe"),
                                company_2.get("roce"),
                                company_2.get("revenue_growth"),
                                company_2.get("profit_growth")
                            ]
                        })

            chart_data = chart_data.set_index("Metric")

            st.bar_chart(
                               chart_data,
                               height=400,
                               stack=False
                        )

                            # ------------------------------------------------
                            # DATA NOTES
                            # ------------------------------------------------

            st.info(
                                "Financial GPS is an educational research tool, "
                                "not a source of personalized investment advice."
                            )

            st.caption(
                                "Financial statement values use each company's "
                                "reported financial currency. Check the currencies "
                                "before comparing monetary amounts across companies. "
                                "Growth figures use the available reported periods."
                            )