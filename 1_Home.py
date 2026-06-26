import streamlit as st

st.set_page_config(page_title="Business Intelligence Portfolio", layout="wide")

st.title("AI Business Intelligence & Strategy Portfolio")
st.markdown("### Bridging Artificial Intelligence with Global Market Dynamics")
st.divider()

col1, col2 = st.columns([2, 1])

with col1:
    st.write("""
    Welcome to my technical portfolio. 
    
    As global supply chains fracture and international markets face severe macroeconomic headwinds, traditional business management is no longer sufficient. Modern corporate strategy requires algorithmic decision-support systems.
    
    This portfolio demonstrates the application of data science and machine learning to solve complex international business friction. 
    
    **Select a module from the sidebar to explore live interactive systems:**
    """)
    
    st.markdown("""
    * **Module 1: Due Diligence Studio** - Automated preliminary M&A and supplier evaluation using NLP heuristics.
    * **Module 2: UK Economic Inactivity Forecast** - Macroeconomic time-series modeling for workforce rehabilitation ROI.
    * **Module 3: ESG Traceability Ledger** - Unsupervised machine learning (Isolation Forest) to detect supply chain greenwashing.
    """)

with col2:
    with st.container(border=True):
        st.write("**Architect Profile**")
        st.write("Syamjith A A")
        st.write("*B.Tech Artificial Intelligence & Data Science*")
        st.divider()
        st.write("**Core Competencies:**")
        st.write("- Corporate Strategy & Risk")
        st.write("- Supply Chain Analytics")
        st.write("- Embedded Finance Infrastructure")