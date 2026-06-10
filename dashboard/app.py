# app.py
# This file: Creates a live interactive website for our intel reporter

import streamlit as st      # streamlit makes websites from Python
import sqlite3              # to read our database
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import COMPANIES

# DB path
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "articles.db")


def get_all_articles():
    """Get all articles from database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT company, title, source, url, published_at, description
        FROM articles
        ORDER BY published_at DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_company_articles(company_name):
    """Get articles for one specific company"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT company, title, source, url, published_at, description
        FROM articles
        WHERE company = ?
        ORDER BY published_at DESC
    """, (company_name,))
    rows = cursor.fetchall()
    conn.close()
    return rows


# ─── PAGE SETUP ───────────────────────────────────────────
# st.set_page_config = sets the browser tab title and layout
st.set_page_config(
    page_title="Intel Reporter",
    page_icon="🔍",
    layout="wide"           # use full screen width
)

# ─── HEADER ───────────────────────────────────────────────
st.title("🔍 AI-Powered Competitive Intelligence Reporter")
st.markdown("**Tracking Indian Fintech Startups in Real Time**")
st.divider()

# ─── SIDEBAR ──────────────────────────────────────────────
# Sidebar = the panel on the left side of the website
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a view:",
    ["📊 Overview", "🏢 Company Deep Dive", "📰 All Articles", "🤖 Run Analysis"]
)

# ─── PAGE 1: OVERVIEW ─────────────────────────────────────
if page == "📊 Overview":

    st.header("📊 Company Overview")

    # Show total articles count
    all_articles = get_all_articles()
    st.metric("Total Articles Collected", len(all_articles))

    st.subheader("Articles per Company")

    # Create columns — one for each company
    cols = st.columns(len(COMPANIES))

    for i, company in enumerate(COMPANIES):
        articles = get_company_articles(company)
        # Each column shows a metric box
        cols[i].metric(
            label=company,
            value=f"{len(articles)} articles"
        )

    st.divider()

    # Show recent articles table
    st.subheader("📰 Recent Articles")
    for article in all_articles[:20]:      # show latest 20
        company  = article[0]
        title    = article[1]
        source   = article[2]
        url      = article[3]
        date     = article[4][:10] if article[4] else "N/A"   # just the date part

        # st.expander = collapsible section
        with st.expander(f"[{company}] {title}"):
            st.write(f"**Source:** {source}")
            st.write(f"**Date:** {date}")
            st.write(f"**URL:** {url}")


# ─── PAGE 2: COMPANY DEEP DIVE ────────────────────────────
elif page == "🏢 Company Deep Dive":

    st.header("🏢 Company Deep Dive")

    # Dropdown to select company
    selected_company = st.selectbox(
        "Select a company to analyze:",
        COMPANIES
    )

    if st.button("🤖 Analyze with AI"):
        # Show loading spinner while AI works
        with st.spinner(f"Analyzing {selected_company}..."):
            from agents.analyzer import analyze_company
            result = analyze_company(selected_company)

        if result:
            st.success("Analysis Complete!")
            st.subheader(f"AI Analysis: {selected_company}")
            # st.text_area shows the analysis in a box
            st.text_area("Results", result["analysis"], height=300)
        else:
            st.error("No articles found for this company")

    # Show articles for selected company
    st.subheader(f"Recent Articles: {selected_company}")
    articles = get_company_articles(selected_company)

    for article in articles:
        title  = article[1]
        source = article[2]
        url    = article[3]
        date   = article[4][:10] if article[4] else "N/A"
        desc   = article[5]

        with st.expander(f"{title}"):
            st.write(f"**Source:** {source} | **Date:** {date}")
            st.write(desc)
            st.write(f"[Read full article]({url})")


# ─── PAGE 3: ALL ARTICLES ─────────────────────────────────
elif page == "📰 All Articles":

    st.header("📰 All Collected Articles")

    # Filter by company
    filter_company = st.selectbox(
        "Filter by company:",
        ["All Companies"] + COMPANIES
    )

    if filter_company == "All Companies":
        articles = get_all_articles()
    else:
        articles = get_company_articles(filter_company)

    st.write(f"Showing {len(articles)} articles")

    for article in articles:
        company = article[0]
        title   = article[1]
        source  = article[2]
        url     = article[3]
        date    = article[4][:10] if article[4] else "N/A"
        desc    = article[5]

        with st.expander(f"[{company}] {title}"):
            st.write(f"**Source:** {source} | **Date:** {date}")
            st.write(desc)
            st.write(f"[Read full article]({url})")


# ─── PAGE 4: RUN ANALYSIS ─────────────────────────────────
elif page == "🤖 Run Analysis":

    st.header("🤖 Run Full AI Analysis")
    st.write("This will analyze all companies and generate a fresh report.")

    if st.button("🚀 Run Full Analysis Now"):
        from agents.analyzer import analyze_all_companies
        from reports.report_generator import generate_html_report, save_report

        with st.spinner("Running AI analysis on all companies..."):
            results = analyze_all_companies()

        with st.spinner("Generating HTML report..."):
            html = generate_html_report(results)
            filepath = save_report(html)

        st.success("Analysis Complete!")
        st.balloons()       # fun celebration animation!

        for company, result in results.items():
            st.subheader(f"📊 {company}")
            st.text_area(
                f"Analysis",
                result["analysis"],
                height=200,
                key=company     # unique key for each text area
            )