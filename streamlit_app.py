import streamlit as st

st.set_page_config(page_title="Data-Driven Mental Health Risk Analysis", page_icon="🧠", layout="wide")

# ---------- Sidebar Navigation ----------
sections = [
    "Overview",
    "Introduction & Objectives",
    "Key Risk Factors and Predictors",
    "Feature-Level Insights",
    "Predictive Modeling Performance",
    "Urban vs. Rural Patterns",
    "Segmentation of Risk Groups",
    "Business Insights",
    "Conclusion",
    "Sources",
]

st.sidebar.title("Navigate")
choice = st.sidebar.radio("Go to:", sections)

# Optional: quick info in sidebar
st.sidebar.markdown("""
**Group Members (Group 1)**

1. Vished — MBA/0075/61  
2. Abhiram Manoj — MBA/0084/61  
3. Harshvardhan Sharma — MBA/0399/61  
4. Anirudh Das — MBA/0413/61
""")


# ---------- Header ----------
st.title("Data-Driven Mental Health Risk Analysis")

# ---------- Section Renderers ----------
if choice == "Overview":
    st.subheader("Project at a Glance")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("AUC (Risk Classifier)", "~0.85")
    c2.metric("Precision", "~0.76")
    c3.metric("Recall", "~0.83")
    c4.metric("Text Classifier Accuracy", "~70%")

    st.markdown(
        """
This app summarizes the team's analysis of mental health risk drivers and modeling results.
Use the left navigation to jump between sections. Key outputs include: major predictors, 
feature-level effects, model performance, geography patterns, risk segment personas, and 
actionable business recommendations.
"""
    )

elif choice == "Introduction & Objectives":
    st.header("Introduction & Objectives")
    st.markdown(
        """
In today’s data-rich environment, demographic, geographic, and lifestyle information can be used
to predict mental health risks and enable proactive interventions. This project integrates two
advanced RNN models to build a decision-support system. Our objectives:

- Identify key risk factors and forecast the likelihood of individuals reporting mental health symptoms.
- Compare patterns across regions (as a proxy for urban vs. rural dynamics).
- Discover risk-based sub-groups via clustering.
- Diagnose mental health disorders from textual statements using an LSTM classifier.

Stakeholders (healthcare providers, employers, educators, NGOs) can use these insights to target
high-risk segments and allocate resources more effectively.
"""
    )

elif choice == "Key Risk Factors and Predictors":
    st.header("Key Risk Factors and Predictors")
    st.markdown(
        """
**Dominant predictors:**
- **Family history of mental illness** — strongest demographic risk factor; associated with higher risk.
- **Access/awareness of care options** — large differences by segment; lower awareness clustered with higher risk.
- **Employment context & self-employment** — self-employed individuals showed elevated risk (stress, less employer support).
- **Gender patterns** — differing reporting/risk patterns across genders in the dataset.
- **Lifestyle factors** — chronic stress and negative habit changes increased risk; supportive work-life habits were protective.
"""
    )

elif choice == "Feature-Level Insights":
    st.header("Feature-Level Insights: Factors Driving Predictions")
    st.markdown("Specific values that push predictions up or down:")

    with st.expander("Countries associated with higher risk"):
        st.markdown("""
- New Zealand (+0.27)  
- Denmark (+0.22)  
- Netherlands (+0.14)  
- South Africa (+0.12)  
- United Kingdom (+0.10)
""")

    with st.expander("Countries associated with lower risk"):
        st.markdown("""
- France (−0.54)  
- Singapore (−0.34)  
- Italy (−0.26)  
- Brazil (−0.11)  
- Switzerland (−0.08)
""")

    with st.expander("Social Weakness"):
        st.markdown("""
- "Yes" slightly increased predicted risk (+0.016).  
- "No" or "Maybe" pushed risk down marginally.
""")

    with st.expander("Growing Stress"):
        st.markdown("""
- "No" pushed predictions up (+0.009) in this dataset (interaction with other strong risk factors).  
- "Maybe" showed the strongest downward effect (−0.008).
""")

    with st.expander("Family History"):
        st.markdown("""
- "Yes" strongly increased predicted risk (+0.061).  
- "No" decreased predicted risk (−0.069).
""")

    with st.expander("Occupation"):
        st.markdown("""
- Business roles had higher relative risk (+0.025).  
- Corporate roles had the strongest downward pull (−0.066).
""")

    with st.expander("Care Options Awareness"):
        st.markdown("""
- Answering "Yes" increased predicted risk (+0.137) — people already at risk may be more aware/engaged.  
- "Not sure" (−0.068) and "No" (−0.033) pulled risk down.
""")

elif choice == "Predictive Modeling Performance":
    st.header("Predictive Modeling Performance")
    st.markdown(
        """
**Multitask RNN (structured data):**
- Classification head: AUC ~0.85, Precision ~0.76, Recall ~0.83.
- Regression head (risk severity score): mean error < 2%.

**Text RNN (LSTM) classifier:**
- ~70% test accuracy across categories (e.g., Anxiety, Depression, Stress, Bipolar, Suicidal, Normal).
- Very strong on "Normal" (94% precision, 86% recall); some confusion among closely related severe categories.

*Interpretation:* Models flag a large majority of at-risk individuals while keeping false positives reasonable, and can
categorize symptoms from language with moderate accuracy (decision-support, not diagnosis).
"""
    )

elif choice == "Urban vs. Rural Patterns":
    st.header("Urban vs. Rural Patterns (via Geography Proxies)")
    st.markdown(
        """
While the dataset did not explicitly label urban vs. rural, **country of residence** was the most significant clustering variable.
Patterns suggest:

- Regions with limited mental health infrastructure showed higher risk and lower awareness of care options.
- Urban/corporate cohorts tended to have more awareness and employer support, correlating with lower risk.
- A high-risk cluster (≈97% predicted probability) featured individuals from a rural-centric country sample with high stress and no employer support.
- Lowest-risk groups included urban tech employees with strong support and awareness.
"""
    )

elif choice == "Segmentation of Risk Groups":
    st.header("Segmentation of Risk Groups (6 Personas)")
    st.markdown("Unsupervised clustering revealed six segments with distinct profiles:")

    with st.expander("Cluster A — High-Risk, High-Support"):
        st.write("~99.5% predicted treatment need; strong family history and symptoms; high awareness/access (e.g., 77% employer options).")

    with st.expander("Cluster B — High-Risk, Low-Support"):
        st.write("≈95% predicted treatment; many self-employed (~50%) and rural; high stress and social withdrawal; limited care awareness.")

    with st.expander("Cluster C — Moderate-Risk, Family-Driven"):
        st.write("Near-universal family history (≈99%); supportive environments; elevated but proactive risk profile with preventive treatment.")

    with st.expander("Cluster D — Chronic Mild Struggles"):
        st.write("Medium risk; occasional mood swings and some stress; maintain work/social interest; suitable for early wellness programs.")

    with st.expander("Cluster E — Low-Risk, Unaware"):
        st.write("Low expressed symptoms and near-zero treatment seeking; low awareness (‘Not sure’ dominant). Potential under-reporting due to stigma.")

    with st.expander("Cluster F — Very Low-Risk, Healthy"):
        st.write("Minimal risk factors; near-zero predicted risk; supportive cultures or younger cohorts; general wellness maintenance.")

elif choice == "Business Insights":
    st.header("Business Insights")
    st.markdown(
        """
**Actionable recommendations:**
- **Targeted interventions:** Outreach for self-employed workers and low-awareness regions (e.g., Cluster B).  
- **Workplace policies:** Expand EAPs, normalize mental health discussions, encourage early help-seeking.  
- **Preventive focus:** Screen and monitor individuals with family predisposition (Cluster C).  
- **Urban–rural allocation:** Invest in rural tele-mental health, primary care training, and anti-stigma programs.  
- **Data-driven monitoring:** Build dashboards to track cohort-level risk and sentiment trends for proactive action.
"""
    )

elif choice == "Conclusion":
    st.header("Conclusion")
    st.markdown(
        """
Integrating AI on multimodal data (surveys + text) offers a comprehensive view of mental health risk. We identified
key drivers, validated predictive performance, and segmented the population into meaningful groups for targeted action.
The goal is to move from reactive to proactive support — improving well-being while reducing costs (absenteeism,
productivity loss, healthcare spend).
"""
    )

elif choice == "Sources":
    st.header("Sources")
    st.markdown(
        """
- https://www.kaggle.com/datasets/bhavikjikadara/mental-health-dataset?resource=download  
- https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health/data  
"""
    )

# ---------- Footer ----------
