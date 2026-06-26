import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# 1. Terminal Configuration
st.set_page_config(page_title="UK Macro-Liquidity Terminal", layout="wide", initial_sidebar_state="expanded")

st.title("🇬🇧 UK Economic Inactivity: 5-Year Algorithmic Forecast")
st.markdown("""
*Dynamic time-series projection modeling the Return on Investment (ROI) of workforce rehabilitation.*  
**Created by:** Syamjith A A 
""")
st.divider()

# 2. Advanced Interactive Sidebar (The Control Panel)
st.sidebar.header("Forecast Parameters")
st.sidebar.markdown("Adjust macroeconomic variables to stress-test the model.")

reintegration_rate = st.sidebar.slider("Annual Reintegration Rate (%)", min_value=1.0, max_value=20.0, value=5.0, step=0.5)
cost_per_worker = st.sidebar.number_input("Govt Intervention Cost per Worker (£)", min_value=1000, max_value=20000, value=5000, step=1000)
wage_inflation = st.sidebar.slider("Estimated Wage Inflation (%)", min_value=1.0, max_value=8.0, value=3.5, step=0.1)

# Base Data
BASE_INACTIVE = 2400000  # Total UK inactive due to long-term sickness
BASE_GDP_CONTRIBUTION = 70000

# 3. Time-Series Algorithmic Forecasting
years = np.arange(2025, 2030)
workers_returned_yearly = []
gross_gdp_generated = []
intervention_costs = []
net_economic_benefit = []

current_inactive = BASE_INACTIVE
current_gdp_cont = BASE_GDP_CONTRIBUTION

for year in years:
    # Calculate workers returning this specific year
    returned_this_year = current_inactive * (reintegration_rate / 100)
    workers_returned_yearly.append(returned_this_year)
    
    # Calculate financials
    gross_gdp = returned_this_year * current_gdp_cont
    cost = returned_this_year * cost_per_worker
    
    gross_gdp_generated.append(gross_gdp)
    intervention_costs.append(cost)
    net_economic_benefit.append(gross_gdp - cost)
    
    # Compound updates for next year
    current_inactive -= returned_this_year
    current_gdp_cont *= (1 + (wage_inflation / 100))

# Create Dynamic DataFrame
df_forecast = pd.DataFrame({
    "Year": years,
    "Workers Reintegrated": workers_returned_yearly,
    "Gross GDP (£ Billions)": [x / 1e9 for x in gross_gdp_generated],
    "Intervention Cost (£ Billions)": [x / 1e9 for x in intervention_costs],
    "Net Economic Benefit (£ Billions)": [x / 1e9 for x in net_economic_benefit]
})

# 4. Executive KPI Dashboard
total_net_benefit = df_forecast["Net Economic Benefit (£ Billions)"].sum()
total_workers = df_forecast["Workers Reintegrated"].sum()
avg_roi = (total_net_benefit / df_forecast["Intervention Cost (£ Billions)"].sum()) * 100

col1, col2, col3, col4 = st.columns(4)
col1.metric("5-Year Net GDP Boost", f"£{total_net_benefit:.2f}B")
col2.metric("Total Workforce Recovered", f"{int(total_workers):,}")
col3.metric("Avg ROI on Intervention", f"{avg_roi:.1f}%")
col4.metric("Ending Inactive Pool", f"{int(current_inactive):,}")

st.markdown("<br>", unsafe_allow_html=True)

# 5. Advanced Visualizations using Plotly
tab1, tab2 = st.tabs(["📈 Financial Trajectory", "📊 Raw Data Export"])

with tab1:
    # Dual Axis Line/Bar Chart
    fig = go.Figure()
    
    # Bar trace for Costs
    fig.add_trace(go.Bar(
        x=df_forecast["Year"], 
        y=df_forecast["Intervention Cost (£ Billions)"],
        name="Intervention Cost",
        marker_color='#ef4444'
    ))
    
    # Line trace for Net Benefit
    fig.add_trace(go.Scatter(
        x=df_forecast["Year"], 
        y=df_forecast["Net Economic Benefit (£ Billions)"],
        name="Net GDP Benefit",
        mode='lines+markers',
        line=dict(color='#22c55e', width=4),
        marker=dict(size=8)
    ))

    fig.update_layout(
        title="Cost vs. GDP Benefit Analysis (2025-2029)",
        xaxis_title="Forecast Year",
        yaxis_title="Pounds (£ Billions)",
        template="plotly_dark",
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.write("Dynamic dataset generated based on current sidebar parameters.")
    st.dataframe(df_forecast.style.format({
        "Workers Reintegrated": "{:,.0f}",
        "Gross GDP (£ Billions)": "£{:.2f}B",
        "Intervention Cost (£ Billions)": "£{:.2f}B",
        "Net Economic Benefit (£ Billions)": "£{:.2f}B"
    }))
    
    # Allow admission officers to download the CSV
    csv = df_forecast.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Forecast Model (CSV)",
        data=csv,
        file_name='uk_gdp_forecast.csv',
        mime='text/csv',
    )
