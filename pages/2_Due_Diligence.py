import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time

# Clean, corporate configuration
st.set_page_config(page_title="Due Diligence Studio", layout="wide")

st.title("AI Business Due Diligence Studio (v1.2)")
st.caption("Automated preliminary evaluation of companies, suppliers, and M&A opportunities using NLP heuristics.")
st.divider()

# 1. Sidebar Inputs (The Intake Form)
st.sidebar.header("Target Profile Intake")
with st.sidebar.form("intake_form"):
    company_name = st.text_input("Entity Name", value="Acme Industrial Solutions")
    industry = st.selectbox("Primary Industry", ["Advanced Manufacturing", "Fintech", "Supply Chain & Logistics", "Renewable Energy", "SaaS"])
    country = st.selectbox("Jurisdiction", ["United Kingdom", "Australia", "New Zealand", "India", "Germany"])
    
    st.write("Strategic Context")
    business_model = st.text_area("Business Model / Description", value="B2B supplier of precision machined components for the aerospace sector.")
    objective = st.selectbox("Diligence Objective", ["Merger & Acquisition (M&A)", "Supplier Vetting", "Venture Capital Investment", "Competitor Analysis"])
    
    submitted = st.form_submit_button("Initiate AI Analysis Pipeline")

# 2. Main Display & Processing
if not submitted:
    # Landing state showing your excellent project overview
    st.subheader("System Architecture & Objective")
    st.write("""
    This platform serves as a decision-support system that accelerates the preliminary research process for cross-border transactions. 
    By standardizing the intake of entity data, the system evaluates:
    * **Strategic Positioning & Business Model Viability**
    * **Operational & Jurisdictional Risks**
    * **Technological Readiness & ESG Compliance**
    
    *Enter target entity parameters in the sidebar to generate a preliminary diligence dossier.*
    """)
else:
    # Simulate API call latency for authenticity
    with st.spinner("Compiling cross-border regulatory frameworks..."):
        time.sleep(1.2)
    with st.spinner("Running semantic analysis on business model..."):
        time.sleep(1.5)
        
    st.success(f"Dossier Generated: {company_name} ({industry} - {country})")
    
    # 3. Executive Dashboard (Metrics & Radar Chart)
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.subheader("Executive Summary")
        st.write(f"**Target:** {company_name} operating within the {industry} sector in {country}.")
        st.write(f"**Objective:** {objective}")
        st.info("Initial algorithmic pass indicates a moderate-to-high viability score, contingent on supply chain resilience and local labor market conditions. The entity's B2B focus requires deep-tier supplier verification.")
        
        st.write("**Automated Risk Flags:**")
        st.warning("⚠️ **Jurisdictional Risk:** Labor market tightness in target region.")
        st.success("✅ **Tech Readiness:** Legacy system integration appears standard.")

    with col2:
        st.subheader("Multi-Dimensional Risk & Health Matrix")
        # Dynamic Radar Chart using Plotly
        categories = ['Market Viability', 'Operational Risk', 'Financial Health', 'Tech Readiness', 'ESG Compliance']
        # Simulated dynamic scoring based on inputs
        scores = [85, 60, 75, 80, 70] if industry != "Fintech" else [90, 80, 85, 95, 60]
        
        fig = go.Figure(data=go.Scatterpolar(
          r=scores + [scores[0]], # close the loop
          theta=categories + [categories[0]],
          fill='toself',
          line=dict(color='#2563eb'),
          fillcolor='rgba(37, 99, 235, 0.2)'
        ))
        fig.update_layout(
          polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
          showlegend=False,
          height=350,
          margin=dict(l=40, r=40, t=20, b=20)
        )
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # 4. Strategic SWOT Analysis Grid
    st.subheader("Algorithmic SWOT Synthesis")
    c_swot1, c_swot2 = st.columns(2)
    
    with c_swot1:
        with st.container(border=True):
            st.write("### Strengths (Internal)")
            st.write(f"• Established operational footprint in {country}.")
            st.write(f"• Alignment with core {industry} growth metrics.")
            st.write("• Clear B2B value proposition.")
            
        with st.container(border=True):
            st.write("### Opportunities (External)")
            st.write("• Expansion into adjacent cross-border markets.")
            st.write("• Digitization of legacy procurement workflows.")

    with c_swot2:
        with st.container(border=True):
            st.write("### Weaknesses (Internal)")
            st.write("• Potential capital lock-up in accounts receivable.")
            st.write("• High dependency on tier-1 raw material suppliers.")
            
        with st.container(border=True):
            st.write("### Threats (External)")
            st.write(f"• Shifting ESG regulatory frameworks in {country}.")
            st.write("• Macroeconomic interest rate volatility impacting CapEx.")

    # 5. Recommendation & Export
    st.divider()
    st.subheader("Phase 2 Investigation Directives")
    st.write("Based on this preliminary assessment, human analysts should prioritize the following areas during deep diligence:")
    st.markdown("- [ ] **Financial Audit:** Request 36-month trailing cash flow statements focusing on working capital cycles.")
    st.markdown("- [ ] **Supply Chain Map:** Identify single-point-of-failure vendors in their manufacturing process.")
    st.markdown("- [ ] **Compliance Review:** Verify ISO certifications and modern slavery act compliance.")
    
    st.download_button(
        label="📥 Export Complete Dossier (CSV)",
        data=pd.DataFrame({"Category": categories, "Score": scores}).to_csv(index=False).encode('utf-8'),
        file_name=f"{company_name.replace(' ', '_')}_Diligence.csv",
        mime='text/csv',
    )