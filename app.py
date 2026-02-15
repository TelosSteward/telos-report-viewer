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
    }
    iframe {
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load the HTML report
report_path = Path(__file__).parent / "report.html"

if not report_path.exists():
    st.error("Report file not found. Place TELOS_Governance_Report_Interactive.html as report.html in this directory.")
    st.stop()

html_content = report_path.read_text(encoding="utf-8")

# Render the full HTML report inside a Streamlit component
st.components.v1.html(html_content, height=2400, scrolling=True)
