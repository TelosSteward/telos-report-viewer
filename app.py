"""
TELOS AI Labs — Governance Demo Hub
Multi-client demo viewer with interactive reports and video walkthroughs.
"""
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="TELOS Governance Demo",
    page_icon="\U0001f512",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Custom CSS ---
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #00d4aa;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #888;
        margin-top: 0;
        margin-bottom: 2rem;
    }
    .video-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #fafafa;
        margin-top: 1.5rem;
        margin-bottom: 0.3rem;
    }
    .video-desc {
        font-size: 0.9rem;
        color: #aaa;
        margin-bottom: 0.8rem;
    }
    .disclaimer {
        font-size: 0.8rem;
        color: #666;
        border: 1px solid #333;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 2rem;
    }
    video { border-radius: 8px; border: 1px solid #333; }
    iframe { border: none; }
</style>
""", unsafe_allow_html=True)

# --- Demo Groups ---
DEMO_ROOT = Path(__file__).parent

DEMO_GROUPS = {
    "Nearmap": {
        "path": "nearmap",
        "subtitle": "Property Intelligence \u2014 Insurance + Solar",
        "has_report": True,
        "videos": [
            {
                "file": "telos_nearmap_demo.mp4",
                "title": "Live Governance Demo",
                "desc": "Full 5-act demo. Two AI agents governed in real-time. "
                        "TELOS scores each request in <30ms, TELOSCOPE independently "
                        "audits every decision. The data is real \u2014 the scenarios are simulated.",
            },
            {
                "file": "telos_forensic_trace.mp4",
                "title": "Forensic Trace Analysis",
                "desc": "SHA-256 hash chain walkthrough. CHAIN INTEGRITY VERIFIED. "
                        "SAAI Framework compliance. Per-turn fidelity scoring with "
                        "intervention log. Every event independently verified.",
            },
            {
                "file": "telos_audit_report_1.mp4",
                "title": "Governance Audit Report \u2014 Insurance",
                "desc": "Interactive HTML governance report for the Insurance domain. "
                        "Scoring distributions, verdict breakdown, chain integrity.",
            },
            {
                "file": "telos_audit_report_2.mp4",
                "title": "Governance Audit Report \u2014 Solar",
                "desc": "Interactive HTML governance report for the Solar domain. "
                        "Same engine, different purpose \u2014 governance adapts automatically.",
            },
        ],
    },
}

# --- Sidebar: Group Selection ---
st.sidebar.markdown("### Demo Groups")
group_names = list(DEMO_GROUPS.keys())
selected_group = st.sidebar.radio(
    "Select a client demo:",
    group_names,
    index=0,
    label_visibility="collapsed",
)

group = DEMO_GROUPS[selected_group]
group_path = DEMO_ROOT / group["path"]

# --- Sidebar: View Toggle ---
st.sidebar.markdown("---")
views = ["Videos"]
if group.get("has_report"):
    views.append("Interactive Report")
selected_view = st.sidebar.radio("View:", views, index=0)

# --- Header ---
st.markdown('<div class="main-header">TELOS Governance Demo</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-header">{} \u2014 {}</div>'.format(selected_group, group["subtitle"]),
    unsafe_allow_html=True,
)

# --- Videos View ---
if selected_view == "Videos":
    st.markdown("""
Two AI agents. Two purposes. Same governance engine.
Every decision scored in <30ms \u2014 **before** the agent acts, not retroactively.
Purpose alignment measured mathematically, not through rules or keyword filters,
with every decision cryptographically signed and traceable.
    """)
    st.divider()

    for demo in group["videos"]:
        video_path = group_path / "videos" / demo["file"]
        st.markdown(
            '<div class="video-title">{}</div>'.format(demo["title"]),
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="video-desc">{}</div>'.format(demo["desc"]),
            unsafe_allow_html=True,
        )
        if video_path.exists():
            st.video(str(video_path))
        else:
            st.warning("Video not found: {}".format(demo["file"]))
        st.divider()

    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Governance Latency", "<30ms", "per request")
    with col2:
        st.metric("Scoring Cascade", "4 layers", "L0\u2192L1\u2192L1.5\u2192L2")
    with col3:
        st.metric("Audit Trail", "SHA-256", "tamper-evident")
    with col4:
        st.metric("Session Proof", "Ed25519", "cryptographic")

# --- Interactive Report View ---
elif selected_view == "Interactive Report":
    report_path = group_path / "report.html"
    if report_path.exists():
        html_content = report_path.read_text(encoding="utf-8")
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
        st.components.v1.html(html_content, height=4000, scrolling=True)
    else:
        st.warning("Interactive report not found for this demo group.")

# --- Footer ---
st.divider()

st.markdown("### What TELOS Demonstrates")
st.markdown("""
- **Purpose Alignment** \u2014 Each agent has a mathematically defined purpose attractor.
  Every request is scored against it in real-time.
- **Boundary Enforcement** \u2014 Hard constraints enforced structurally, not behaviorally.
- **Cryptographic Audit** \u2014 HMAC-SHA512 signed decisions. Ed25519 session proof.
  SHA-256 tamper-evident hash chain.
- **Independent Measurement** \u2014 TELOSCOPE audits the governance engine using a
  separate instrument and methodology.
- **Regulatory Readiness** \u2014 A measurement hedge against regulatory uncertainty.
  As AI governance regulations form, TELOS provides the cryptographic evidence trail.
""")

st.markdown("""
<div class="disclaimer">
<strong>DISCLAIMER</strong><br>
Demonstrations use simulated scenarios built from publicly available information.
No client systems, APIs, or proprietary data are accessed. Property data, detection layers,
and tool definitions are simulated composites derived from public records, published product
documentation, and industry-standard terminology.
The purpose is to demonstrate TELOS governance capabilities.
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "**TELOS AI Labs** | [GitHub](https://github.com/TelosSteward) | Built with purpose alignment."
)
