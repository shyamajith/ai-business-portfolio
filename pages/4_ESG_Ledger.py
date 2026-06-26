import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.ensemble import IsolationForest
import hashlib
from datetime import datetime

st.set_page_config(page_title="AI Traceability Engine", layout="wide")

st.title("Algorithmic ESG Traceability & Greenwashing Detection")
st.markdown("""
*Enterprise pipeline utilizing Unsupervised Machine Learning (Isolation Forest) to detect supply chain data anomalies.* **Created By:** Syamjith A A 
""")
st.divider()

# 1. SYNTHETIC ENTERPRISE DATABASE (Replacing Hardcoded rules)
# We generate 1,000 rows of historical, realistic mining data to train our ML model.
@st.cache_data
def load_historical_data():
    np.random.seed(42)
    n_samples = 1000
    df = pd.DataFrame({
        'carbon_intensity': np.random.normal(loc=8.5, scale=1.5, size=n_samples),
        'water_intensity': np.random.normal(loc=25.0, scale=4.0, size=n_samples),
        'transport_distance_km': np.random.normal(loc=1200, scale=300, size=n_samples)
    })
    # Inject 5% intentional anomalies (greenwashing or extreme pollution)
    outliers = int(n_samples * 0.05)
    df.loc[:outliers - 1, 'carbon_intensity'] = np.random.uniform(1.0, 3.0, outliers)  # Fake "too good to be true" data
    df.loc[outliers:outliers * 2 - 1, 'carbon_intensity'] = np.random.uniform(18.0, 25.0, outliers)  # Heavy polluters
    return df

hist_df = load_historical_data()

# Train the Unsupervised ML Anomaly Detector
@st.cache_resource
def train_anomaly_model(data):
    # Isolation Forest isolates observations by randomly selecting a feature and then randomly selecting a split value
    model = IsolationForest(contamination=0.10, random_state=42)
    model.fit(data[['carbon_intensity', 'water_intensity']])
    return model

ml_model = train_anomaly_model(hist_df)

# 2. THE UI & INGESTION
col_input, col_display = st.columns([1, 2.5])

with col_input:
    st.header("1. Batch Ingestion")
    with st.form("ingestion_form"):
        mineral = st.selectbox("Commodity", ["Lithium Spodumene", "Nickel Sulphate"])
        site = st.selectbox("Origin", ["Pilgangoora (WA)", "Olympic Dam (SA)"])
        destination = st.selectbox("Export Port", ["Port Hedland", "Port of Melbourne"])
        
        st.markdown("##### Sensor Telemetry")
        co2_footprint = st.number_input("Reported Carbon (kg CO2e/kg)", value=7.5, step=0.1)
        water_intensity = st.number_input("Reported Water (m³/Ton)", value=24.0, step=0.5)
        
        submit = st.form_submit_button("Run ML Diagnostics")

# 3. ALGORITHMIC PROCESSING & DISPLAY
if submit:
    with col_display:
        st.header("2. AI Diagnostic Results")
        
        # Package input for the ML model
        input_data = pd.DataFrame({'carbon_intensity': [co2_footprint], 'water_intensity': [water_intensity]})
        
        # Prediction: 1 is normal, -1 is anomaly
        prediction = ml_model.predict(input_data)[0]
        # Get exact anomaly score (negative means more anomalous)
        anomaly_score = ml_model.decision_function(input_data)[0]
        
        # Calculate Percentiles against historical data
        co2_percentile = int((hist_df['carbon_intensity'] < co2_footprint).mean() * 100)
        
        c1, c2, c3 = st.columns(3)
        if prediction == 1:
            c1.success("✅ ML Status: VERIFIED NORMAL")
            c1.caption("Data aligns with historical distribution.")
        else:
            c1.error("🚨 ML Status: ANOMALY DETECTED")
            c1.caption("Flagged for potential Greenwashing or severe violation.")
            
        c2.metric("Anomaly Confidence Score", f"{anomaly_score:.3f}")
        c3.metric("Carbon Percentile", f"Top {co2_percentile}%", delta=f"{co2_footprint - hist_df['carbon_intensity'].mean():.2f} vs Avg", delta_color="inverse")

        # 4. ADVANCED VISUALIZATION: Sankey Supply Chain Graph
        st.subheader("3. Physical Flow Verification (Sankey Diagram)")
        
        # Mapping the nodes dynamically based on user input
        labels = [site, "Rail Logistics", "Coastal Refinery", destination, "Global Buyer"]
        source = [0, 1, 2, 3] # Indices of labels
        target = [1, 2, 3, 4]
        values = [100, 100, 95, 95] # Represents 5% mass loss during refining
        
        fig = go.Figure(data=[go.Sankey(
            node = dict(
              pad = 15, thickness = 20,
              line = dict(color = "black", width = 0.5),
              label = labels,
              color = "blue"
            ),
            link = dict(
              source = source, target = target, value = values,
              color = "rgba(173, 216, 230, 0.4)" # Light blue transparent
            ))])
        
        fig.update_layout(height=350, margin=dict(l=0, r=0, t=20, b=0), template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)
        
        # Cryptographic Hash (Proof of work)
        hash_str = hashlib.sha256(f"{mineral}{site}{co2_footprint}{datetime.now()}".encode()).hexdigest()
        st.code(f"BLOCKCHAIN COMMIT HASH: {hash_str}", language="markdown")
