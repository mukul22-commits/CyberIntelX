import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import subprocess

from login import login_page

from logout import (
    logout_button
)

from complaint_form import complaint_form

from investigation_panel import investigation_panel

from track_complaint import track_complaint

from officer_analytics import officer_analytics

from export_complaints import export_complaints

from notification_center import notification_center

from case_assignment_dashboard import case_assignment_dashboard

from intelligence_report import (
    generate_intelligence_report
)

from officer_portal import officer_portal

from heatmap_dashboard import heatmap_dashboard

from officer_performance import officer_performance

from alert_center import alert_center

from fraud_prediction import fraud_prediction

from ioc_correlation_dashboard import (
    ioc_correlation_dashboard
)

from ai_assistant_dashboard import (
    ai_assistant_dashboard
)

from link_analysis_dashboard import (
    link_analysis_dashboard
)

from threat_actor_dashboard import (
    threat_actor_dashboard
)

from entity_resolution_dashboard import (
    entity_resolution_dashboard
)

from fraud_ring_dashboard import fraud_ring_dashboard

from case_prioritization_dashboard import case_prioritization_dashboard

from campaign_dashboard import campaign_dashboard

from threat_monitoring_dashboard import threat_monitoring_dashboard

from executive_dashboard import executive_dashboard

from timeline_dashboard import timeline_dashboard

from intelligence_score_dashboard import intelligence_score_dashboard

from ioc_enrichment_dashboard import ioc_enrichment_dashboard

from domain_intelligence_dashboard import (
    domain_intelligence_dashboard
)

from email_intelligence_dashboard import (
    email_intelligence_dashboard
)

from hash_intelligence_dashboard import (
    hash_intelligence_dashboard
)

from verification_dashboard import (
    verification_dashboard
)

from investigation_confidence_dashboard import (
    investigation_confidence_dashboard
)

from ai_report_dashboard import (
    ai_report_dashboard
)

from case_intelligence_dashboard import (
    case_intelligence_dashboard
)

from intelligence_normalizer_dashboard import (
    intelligence_normalizer_dashboard
)

from intelligence_correlation_dashboard import (
    intelligence_correlation_dashboard
)

from threat_cluster_dashboard import (
    threat_cluster_dashboard
)

from national_threat_center import (
    national_threat_center
)

from alert_engine_dashboard import (
    alert_engine_dashboard
)

from cyber_fusion_center import (
    cyber_fusion_center
)

from ioc_reputation_dashboard import ioc_reputation_dashboard

from active_incident_center import (
    active_incident_center
)

from vulnerability_intelligence import vulnerability_intelligence

from daily_brief_dashboard import (
    daily_brief_dashboard
)

from whois_dashboard import (
    whois_dashboard
)

from geoip_dashboard import geoip_dashboard

from dashboard.officer_management import officer_management

from dashboard.investigator_workspace import investigator_workspace

from threat_trend_dashboard import (
    threat_trend_dashboard
)

from sector_risk_dashboard import (
    sector_risk_dashboard
)

from threat_forecast_dashboard import (
    threat_forecast_dashboard
)

from attack_surface_dashboard import (
    attack_surface_dashboard
)

from ioc_fusion_dashboard import (
    ioc_fusion_dashboard
)

from advanced_correlation_dashboard import (
    advanced_correlation_dashboard
)

from incident_intelligence_dashboard import (
    incident_intelligence_dashboard
)

from vulnerability_dashboard import (
    vulnerability_dashboard
)

from threat_score_dashboard import (
    threat_score_dashboard
)

from case_timeline_dashboard import (
    case_timeline_dashboard
)

from virustotal_dashboard import (
    virustotal_dashboard
)


from my_complaints import (
    my_complaints
)

from dashboard.victim_dashboard import (
    victim_dashboard
)

from dashboard.ioc_fusion_v2_dashboard import (
    ioc_fusion_v2_dashboard
)

from threat_intelligence_workbench import (
    threat_intelligence_workbench
)

from officer_assignment_dashboard import (
    officer_assignment_dashboard
)

from cyber_fusion_v2 import (
    cyber_fusion_v2
)

from chain_of_custody_dashboard import (
    chain_of_custody_dashboard
)

from report_center import (
    report_center
)

from executive_situation_room import (
    executive_situation_room
)

from threat_wall import (
    threat_wall
)

from dashboard.cyber_theme import (
    apply_cyber_theme
)

from mitre_dashboard import (
    mitre_dashboard
)

from officer_workload_dashboard import (
    officer_workload_dashboard
)

from case_command_center import (
    case_command_center
)

from analyst_operations_center import (
    analyst_operations_center
)

from fusion_center_home import (
    fusion_center_home
)

from navigation import (
    navigation_menu
)

from navigation_hub import (
    navigation_hub
)


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Cyber Crime Intelligence Dashboard",
    page_icon="🛡️",
    layout="wide"
)

apply_cyber_theme()

# =====================================
# SESSION MANAGEMENT
# =====================================

if "logged_in" not in st.session_state:

    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:

    login_page()

    st.stop()
# =====================================
# CUSTOM CSS
# =====================================

st.markdown(
    """
<style>

.main {
    background-color: #0E1117;
}

div[data-testid="metric-container"] {
    background-color: #1E1E1E;
    border: 1px solid #2E2E2E;
    padding: 15px;
    border-radius: 12px;
}

</style>
""",
    unsafe_allow_html=True
)

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title(
    "🛡️ Cyber Cell Portal"
)

role = st.session_state["role"]

allowed_roles = [
    "Admin",
    "Officer",
    "Victim",
    "Analyst",
    "Viewer"
]

if role not in allowed_roles:

    st.error(
        "Invalid Role"
    )

    st.stop()

st.sidebar.success(
    f"""
User: {st.session_state['username']}

Role: {role}
"""
)

logout_button()

# =====================================
# VICTIM PORTAL
# =====================================

if role == "Victim":

    st.sidebar.success(
        "Victim Portal"
    )

    page = st.sidebar.radio(
        "Menu",
        [
            "Submit Complaint",
            "My Complaints"
        ]
    )

    if page == "Submit Complaint":

        complaint_form()

    if page == "My Complaints":

        victim_dashboard()

    st.stop()

# =====================================
# OFFICER PORTAL
# =====================================

if role == "Officer":

    officer_portal()

    st.stop()




# =====================================
# ADMIN MENU
# =====================================

page = navigation_menu()

if "page" in st.session_state:

    page = st.session_state["page"]


# =====================================
# COMPLAINT ANALYTICS
# =====================================

if page == "Complaint Analytics":

    st.title("📋 Complaint Analytics Dashboard")

    conn = sqlite3.connect(
       "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    total_complaints = len(complaints)

    high_risk_complaints = len(
        complaints[
            complaints["risk_score"] >= 70
        ]
    )

    avg_risk = round(
        complaints["risk_score"].mean(),
        2
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Total Complaints",
        total_complaints
    )

    c2.metric(
        "High Risk Complaints",
        high_risk_complaints
    )

    c3.metric(
        "Average Risk Score",
        avg_risk
    )

    st.markdown("---")

    if st.button("Export Complaints CSV"):

        csv_file = export_complaints()

        st.success(
            f"Exported: {csv_file}"
        )

    st.markdown("---")

    left, right = st.columns(2)

    with left:

        st.subheader(
            "Complaint Categories"
        )

        category_df = (
            complaints["category"]
            .value_counts()
            .reset_index()
        )

        category_df.columns = [
            "Category",
            "Count"
        ]

        fig = px.pie(
            category_df,
            names="Category",
            values="Count"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    with right:

        st.subheader(
            "State Wise Complaints"
        )

        state_df = (
            complaints["state"]
            .value_counts()
            .reset_index()
        )

        state_df.columns = [
            "State",
            "Count"
        ]

        fig = px.bar(
            state_df,
            x="State",
            y="Count"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    st.markdown("---")

    st.subheader(
        "Complaint Investigation Queue"
    )

    st.dataframe(
        complaints[
            [
                "id",
                "name",
                "category",
                "state",
                "risk_score",
                "created_at"
            ]
        ],
        width="stretch"
    )

    st.markdown("---")

    st.subheader(
        "Evidence Repository"
    )

    for _, row in complaints.iterrows():

        st.write(
            f"Complaint #{row['id']} | {row['name']}"
        )

        st.write(
            f"Evidence: {row['evidence_file']}"
        )

    st.stop()

# =====================================
# INVESTIGATION PANEL
# =====================================

if page == "Fusion Center Home":

    fusion_center_home()

    st.stop()

if page == "Investigation Panel":
    investigation_panel()
    st.stop()

if page == "Officer Analytics":
    officer_analytics()
    st.stop()

if page == "Officer Performance":

    officer_performance()

    st.stop()

if page == "Officer Workload":

    officer_workload_dashboard()

    st.stop()

if page == "Officer Management":

    if role != "Admin":

        st.error(
            "Access Denied"
        )

        st.stop()

    officer_management()

    st.stop()

if page == "Officer Assignment Center":

    officer_assignment_dashboard()

    st.stop()


if page == "Case Assignment Dashboard":

    case_assignment_dashboard()

    st.stop()

if page == "Cyber Crime Heatmap":

    heatmap_dashboard()

    st.stop()

if page == "Alert Center":

    alert_center()

    st.stop()

if page == "Fraud Trend Prediction":

    fraud_prediction()

    st.stop()

if page == "AI Investigation Assistant":

    ai_assistant_dashboard()

    st.stop()

if page == "Link Analysis Graph":

    link_analysis_dashboard()

    st.stop()


if page == "Threat Actor Intelligence":

    threat_actor_dashboard()

    st.stop()
if page == "Entity Resolution Center":

    entity_resolution_dashboard()

    st.stop()

if page == "Fraud Ring Intelligence":

    fraud_ring_dashboard()

    st.stop()

if page == "Case Prioritization Center":

    case_prioritization_dashboard()

    st.stop()

if page == "Campaign Intelligence":

    campaign_dashboard()

    st.stop()

if page == "National Cyber Threat Monitoring Center":

    threat_monitoring_dashboard()

    st.stop()

if page == "MITRE ATT&CK Mapping":

    mitre_dashboard()

    st.stop()

if page == "Executive Intelligence Dashboard":

    executive_dashboard()

    st.stop()

if page == "Investigation Timeline":

    timeline_dashboard()

    st.stop()

if page == "Intelligence Scoring Center":

    intelligence_score_dashboard()

    st.stop()

if page == "IOC Enrichment Center":

    ioc_enrichment_dashboard()

    st.stop()

if page == "Domain Intelligence":

    domain_intelligence_dashboard()

    st.stop()

if page == "Email Intelligence":

    email_intelligence_dashboard()

    st.stop()

if page == "Hash Intelligence":

    hash_intelligence_dashboard()

    st.stop()

if page == "VirusTotal Intelligence":

    virustotal_dashboard()

    st.stop()


if page == "Verification Center":

    verification_dashboard()

    st.stop()

if page == "Investigation Confidence":

    investigation_confidence_dashboard()

    st.stop()

if page == "AI Intelligence Report":

    ai_report_dashboard()

    st.stop()

if page == "Case Intelligence Center":

    case_intelligence_dashboard()

    st.stop()

if page == "Intelligence Normalization":

    intelligence_normalizer_dashboard()

    st.stop()

if page == "Intelligence Correlation":

    intelligence_correlation_dashboard()

    st.stop()

if page == "Threat Clusters":

    threat_cluster_dashboard()

    st.stop()

if page == "National Threat Center":

    national_threat_center()

    st.stop()

if page == "Automated Alert Center":

    alert_engine_dashboard()

    st.stop()

if page == "Cyber Fusion Center":

    cyber_fusion_center()

    st.stop()

if page == "IOC Reputation Center":

    ioc_reputation_dashboard()

    st.stop()

if page == "Active Incident Center":

    active_incident_center()

    st.stop()

if page == "Vulnerability Intelligence Center":

    vulnerability_intelligence()

    st.stop()

if page == "Daily Intelligence Brief":

    daily_brief_dashboard()

    st.stop()

if page == "WHOIS Intelligence":

    whois_dashboard()

    st.stop()

if page == "Geo-IP Intelligence":

    geoip_dashboard()

    st.stop()

if page == "Investigator Workspace":

    investigator_workspace()

    st.stop()

if page == "Threat Trend Center":

    threat_trend_dashboard()

    st.stop()

if page == "Sector Risk Center":

    sector_risk_dashboard()

    st.stop()

if page == "Threat Forecast Center":

    threat_forecast_dashboard()

    st.stop()

if page == "Attack Surface Center":

    attack_surface_dashboard()

    st.stop()

if page == "IOC Fusion Center":

    ioc_fusion_dashboard()

    st.stop()

if page == "Advanced Correlation":

    advanced_correlation_dashboard()

    st.stop()

if page == "Incident Intelligence":

    incident_intelligence_dashboard()

    st.stop()

if page == "Vulnerability Intelligence":

    vulnerability_dashboard()

    st.stop()

if page == "Threat Score Center":

    threat_score_dashboard()

    st.stop()

if page == "Case Timeline":

    case_timeline_dashboard()

    st.stop()

if page == "IOC Fusion Intelligence":

    ioc_fusion_v2_dashboard()

    st.stop()

if page == "Threat Intelligence Workbench":

    threat_intelligence_workbench()

    st.stop()

if page == "Analyst Operations Center":

    analyst_operations_center()

    st.stop()

if page == "Cyber Fusion Command Center":

    cyber_fusion_v2()

    st.stop()

if page == "Chain Of Custody":

    chain_of_custody_dashboard()

    st.stop()

if page == "Executive Situation Room":

    st.success("EXECUTIVE ROOM LOADED")

    executive_situation_room()

    st.stop()

if page == "National Threat Wall":

    st.success("THREAT WALL LOADED")

    threat_wall()

    st.stop()

if page == "Investigation Report Center":

    report_center()

    st.stop()

if page == "MITRE ATT&CK Intelligence":

    mitre_dashboard()

    st.stop()

if page == "IOC Correlation Center":

    ioc_correlation_dashboard()

    st.stop()

if page == "Case Command Center":

    st.success("CASE COMMAND CENTER LOADED")

    case_command_center()

    st.stop()

# =====================================
# DATABASE
# =====================================

conn = sqlite3.connect(
    "database/cybercrime.db"
)

df = pd.read_sql(
    "SELECT * FROM intelligence_data",
    conn
)

conn.close()

# =====================================
# HEADER
# =====================================

st.title(
    "🛡️ Cyber Crime Intelligence & Threat Monitoring Dashboard"
)

st.caption(
    "Cyber Cell Intelligence Platform"
)

notification_center()

if st.button(
    "Generate Weekly Intelligence Report"
):

    pdf_file = (
        generate_intelligence_report()
    )

    st.success(
        f"Report Generated: {pdf_file}"
    )

st.markdown("---")
# =====================================
# KPI CALCULATIONS
# =====================================

total_articles = len(df)

high_risk = len(
    df[df["threat_score"] >= 30]
)

avg_score = round(
    df["threat_score"].mean(),
    2
)

keywords = [
    "phishing",
    "ransomware",
    "malware",
    "botnet",
    "fraud",
    "exploit",
    "zero-day",
    "cve"
]

keyword_count = {}

for keyword in keywords:

    keyword_count[keyword] = (
        df["title"]
        .str.lower()
        .str.contains(keyword)
        .sum()
    )

top_keyword = max(
    keyword_count,
    key=keyword_count.get
)

# =====================================
# KPI DISPLAY
# =====================================

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Total Articles",
    total_articles
)

c2.metric(
    "High Risk Articles",
    high_risk
)

c3.metric(
    "Average Threat Score",
    avg_score
)

c4.metric(
    "Top Threat Keyword",
    top_keyword
)

# =====================================
# THREAT SEVERITY
# =====================================

def severity(score):

    if score >= 80:
        return "Critical"

    elif score >= 50:
        return "High"

    elif score >= 20:
        return "Medium"

    else:
        return "Low"


df["severity"] = (
    df["threat_score"]
    .apply(severity)
)

# =====================================
# CHARTS ROW 1
# =====================================

left, right = st.columns(2)

with left:

    st.subheader(
        "Threat Score Distribution"
    )

    fig = px.histogram(
        df,
        x="threat_score"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

with right:

    st.subheader(
        "Sentiment Distribution"
    )

    sentiment = (
        df["sentiment"]
        .value_counts()
        .reset_index()
    )

    sentiment.columns = [
        "Sentiment",
        "Count"
    ]

    fig = px.pie(
        sentiment,
        names="Sentiment",
        values="Count"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

# =====================================
# CHARTS ROW 2
# =====================================

left, right = st.columns(2)

with left:

    st.subheader(
        "Threat Severity Breakdown"
    )

    sev = (
        df["severity"]
        .value_counts()
        .reset_index()
    )

    sev.columns = [
        "Severity",
        "Count"
    ]

    fig = px.bar(
        sev,
        x="Severity",
        y="Count"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

with right:

    st.subheader(
        "Threat Keyword Frequency"
    )

    keyword_df = pd.DataFrame(
        {
            "Keyword": list(keyword_count.keys()),
            "Count": list(keyword_count.values())
        }
    )

    fig = px.bar(
        keyword_df,
        x="Keyword",
        y="Count"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

# =====================================
# ENTITY INTELLIGENCE
# =====================================

try:

    orgs = pd.read_csv(
        "data/top_orgs.csv"
    )

    countries = pd.read_csv(
        "data/top_countries.csv"
    )

    left, right = st.columns(2)

    with left:

        st.subheader(
            "Top Organizations"
        )

        fig = px.bar(
            orgs.head(10),
            x="count",
            y="entity",
            orientation="h"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    with right:

        st.subheader(
            "Top Countries"
        )

        fig = px.bar(
            countries.head(10),
            x="count",
            y="entity",
            orientation="h"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

except:

    st.warning(
        "Entity Intelligence not generated yet."
    )

# =====================================
# AI INTELLIGENCE BRIEF
# =====================================

st.subheader(
    "AI Intelligence Brief"
)

brief = f"""
• Total intelligence articles collected: {total_articles}

• High-risk articles detected: {high_risk}

• Average threat score: {avg_score}

• Most observed threat category: {top_keyword}

• Sentiment profile:
{df['sentiment'].value_counts().to_dict()}
"""

st.info(brief)

if st.button(
    "🔄 Refresh Threat Feed"
):

    subprocess.run(
        [
            "python",
            "collectors/rss_collector.py"
        ]
    )

    st.success(
        "Threat Feed Updated Successfully"
    )


# =====================================
# FEED
# =====================================

st.subheader(
    "🌍 Real-Time Threat Intelligence Feed"
)

latest_feed = pd.read_sql(
    """
    SELECT
        source,
        title,
        link,
        threat_score,
        sentiment
    FROM intelligence_data
    ORDER BY rowid DESC
    LIMIT 20
    """,
    sqlite3.connect(
        "database/cybercrime.db"
    )
)

st.dataframe(
    latest_feed,
    width="stretch"
)