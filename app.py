"""
TELOS Governance Report Viewer
Standalone Streamlit app that serves the interactive governance report.
"""
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="TELOS Governance Report",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome for a clean embed experience
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        max-width: 100%;
    }
    .stApp {
        background-color: #0d1117;
    }
    iframe {
        border: none;
        width: 100%;
        height: 100vh;
        -webkit-overflow-scrolling: touch;
        overflow-y: scroll;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load the HTML report
report_path = Path(__file__).parent / "report.html"

if not report_path.exists():
    st.error("Report file not found.")
    st.stop()

html_content = report_path.read_text(encoding="utf-8")

# Inject mobile-friendly viewport and touch scrolling into the HTML
mobile_fix = """
<style>
html, body {
    overflow-y: auto !important;
    -webkit-overflow-scrolling: touch !important;
    height: auto !important;
    min-height: 100vh;
}
</style>
"""
html_content = html_content.replace("</head>", mobile_fix + "</head>")

# Use a large height so the iframe doesn't clip, with scrolling enabled
st.components.v1.html(html_content, height=4000, scrolling=True)
