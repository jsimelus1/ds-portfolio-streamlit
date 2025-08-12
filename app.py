import json
from pathlib import Path
from datetime import datetime

import streamlit as st
import pandas as pd

# ---------- Page config ----------
st.set_page_config(
    page_title="James Simelus — Data Scientist & Ex-SysAdmin",
    page_icon="📊",
    layout="wide",
)

# ---------- Helpers ----------
ROOT = Path(__file__).parent
PROJECTS_PATH = ROOT / "projects.json"
HEADSHOT = ROOT / "assets" / "headshot.jpg"
RESUME = ROOT / "resume" / "James_Simelus_Resume.pdf"

@st.cache_data
def load_projects() -> list:
    with open(PROJECTS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def chip(text: str):
    st.markdown(
        f"""
        <span class="chip">{text}</span>
        """,
        unsafe_allow_html=True,
    )

# ---------- Styles ----------
st.markdown(
    """
    <style>
    .chip {display:inline-block;padding:6px 10px;border:1px solid #1f2a37;border-radius:999px;margin:4px;background:#0f1520;color:#e8eef7;font-size:13px}
    .muted {color:#a8b3c7}
    .card {padding:16px;border:1px solid #1f2a37;border-radius:14px;background:#121821;}
    .btn a{display:inline-block;padding:8px 12px;border:1px solid #2a3a4f;border-radius:10px;background:#101826;color:#e8eef7;text-decoration:none;margin-right:10px}
    .btn a:hover{border-color:#4da3ff}
    .subtitle{color:#a8b3c7;margin-top:-6px}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Sidebar ----------
st.sidebar.image(str(HEADSHOT))
st.sidebar.markdown("**James Simelus**")
st.sidebar.markdown(
    "M.S. in Data Science & Analytics • Former Windows System Administrator"
)
st.sidebar.markdown("---")
st.sidebar.markdown("**Links**")
st.sidebar.markdown("- [LinkedIn](https://www.linkedin.com/in/YOUR-LINKEDIN)")
st.sidebar.markdown("- [GitHub](https://github.com/YOUR-GITHUB)")
st.sidebar.markdown("- [GitLab](https://gitlab.com/YOUR-GITLAB)")
if RESUME.exists():
    with open(RESUME, "rb") as f:
        st.sidebar.download_button("Download Resume (PDF)", f, file_name=RESUME.name)

# ---------- Header ----------
col1, col2 = st.columns([1, 3])
with col1:
    st.image(str(HEADSHOT))
with col2:
    st.title("James Simelus")
    st.markdown("<p class='subtitle'>Data Scientist & Former Windows System Administrator</p>", unsafe_allow_html=True)
    st.write(
        "I build analytics and ML solutions that are production-ready, secure, and easy to run in enterprise environments."
    )

# ---------- Skills ----------
st.subheader("Skills")
skills = [
    "Python (pandas, scikit-learn, NumPy)",
    "SQL (PostgreSQL)",
    "NLP (spaCy, transformers)",
    "Visualization (Plotly, Matplotlib, Power BI)",
    "ETL & Orchestration",
    "Docker & Kubernetes",
    "Windows Server, AD, GPO",
    "PowerShell Automation",
]

for s in skills:
    chip(s)
st.markdown("<br>", unsafe_allow_html=True)

# ---------- About ----------
st.subheader("About")
st.write(
    """
    I'm a data scientist with a Master's in Data Science & Analytics and years of experience as a Windows System Administrator.\
    My background in AD/Group Policy, PowerShell automation, and server performance helps me deploy reliable, secure data systems.
    """
)

# ---------- Projects ----------
st.subheader("Projects")
projects = load_projects()

# Display projects in a responsive grid-like layout
n_cols = 3
rows = [projects[i : i + n_cols] for i in range(0, len(projects), n_cols)]
for row in rows:
    cols = st.columns(n_cols)
    for col, p in zip(cols, row):
        with col:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown(f"### {p['title']}")
            st.caption(p.get("role", "Project"))
            st.write(p["description"])
            st.markdown("**Tech:** " + ", ".join(p.get("tech", [])))
            st.markdown("<div class='btn'>", unsafe_allow_html=True)
            if p.get("demo"):
                st.markdown(f"[Live Demo]({p['demo']}) ", unsafe_allow_html=True)
            if p.get("repo"):
                st.markdown(f"[Git Repo]({p['repo']}) ", unsafe_allow_html=True)
            if p.get("post"):
                st.markdown(f"[Write-up]({p['post']}) ", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

# ---------- Writing ----------
st.subheader("Writing")
st.markdown("- [From SysAdmin to Data Scientist: Deploying ML That Actually Runs](#)")
st.markdown("- [Hardening a Data Stack: Security Considerations for Analytics Teams](#)")

# ---------- Footer ----------
st.markdown("---")
st.caption(f"© {datetime.now().year} James Simelus • james.simelus@example.com")
