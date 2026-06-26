import plotly.graph_objects as go
import os

st.set_page_config(page_title="Macroeconomic Inactivity", layout="wide")

st.title("Global Workforce Inactivity Forecaster (v3.0)")
st.caption("Cross-border econometric modeling simulating the ROI of governmental and corporate labor rehabilitation. Data fetched dynamically from macro-database.")
st.divider()

# 1. Master Data Management: Dynamic CSV Fetch
@st.cache_data
def load_country_profiles():
    # In enterprise software, you never hardcode data. 
    # We fetch it dynamically from our local CSV database.
    try:
        df = pd.read_csv("global_macro_data.csv")
        profiles = {}
        for index, row in df.iterrows():
            profiles[row['Country']] = {
                "currency": row['Currency'],
                "avg_gdp_per_worker": row['Avg_GDP_Per_Worker'],
                "base_inactive": row['Total_Inactive']
            }
        return profiles
    except FileNotFoundError:
        # Emergency Fallback if the CSV is missing
        st.error("Database connection lost. Loading UK Fallback data.")
        return {"United Kingdom": {"currency": "£", "avg_gdp_per_worker": 75000, "base_inactive": 9400000}}

profiles = load_country_profiles()

# 2. Sidebar Intake
st.sidebar.subheader("Jurisdiction Selection")
selected_country = st.sidebar.selectbox("Target Economy", list(profiles.keys()))

# Extract active profile data
active_profile = profiles[selected_country]
curr = active_profile["currency"]
current_inactive = active_profile["base_inactive"]
current_gdp_cont = active_profile["avg_gdp_per_worker"]

st.sidebar.subheader("Intervention Parameters")
reintegration_rate = st.sidebar.slider("Annual Reintegration Target (%)", 1.0, 20.0, 5.0, 0.5)
cost_per_worker = st.sidebar.number_input(f"Intervention Cost per Worker ({curr})", 1000, 50000, 5000, 500)
wage_inflation = st.sidebar.slider("Estimated Wage Inflation (%)", 1.0, 8.0, 3.5, 0.1)

# 3. Algorithmic Time-Series Forecasting
years = np.arange(2025, 2030)
workers_returned_yearly = []
gross_gdp_generated = []
intervention_costs = []
net_economic_benefit = []

for year in years:
    returned_this_year = current_inactive * (reintegration_rate / 100)
    workers_returned_yearly.append(returned_this_year)
    
    gross_gdp = returned_this_year * current_gdp_cont
    cost = returned_this_year * cost_per_worker
    
    gross_gdp_generated.append(gross_gdp)
    intervention_costs.append(cost)
    net_economic_benefit.append(gross_gdp - cost)
    
    # Compound updates
    current_inactive -= returned_this_year
    current_gdp_cont *= (1 + (wage_inflation / 100))

df_forecast = pd.DataFrame({
    "Year": years,
    "Workers Reintegrated": workers_returned_yearly,
    "Gross GDP (Billions)": [x / 1e9 for x in gross_gdp_generated],
    "Intervention Cost (Billions)": [x / 1e9 for x in intervention_costs],
    "Net Economic Benefit (Billions)": [x / 1e9 for x in net_economic_benefit]
})

# 4. Executive KPI Dashboard
total_net_benefit = df_forecast["Net Economic Benefit (Billions)"].sum()
total_workers = df_forecast["Workers Reintegrated"].sum()
avg_roi = (total_net_benefit / df_forecast["Intervention Cost (Billions)"].sum()) * 100

st.subheader(f"{selected_country} Economic Projections (2025-2029)")
col1, col2, col3, col4 = st.columns(4)
col1.metric("5-Year Net GDP Boost", f"{curr}{total_net_benefit:.2f}B")
col2.metric("Total Workforce Recovered", f"{int(total_workers):,}")
col3.metric("Avg ROI on Intervention", f"{avg_roi:.1f}%")
col4.metric("Remaining Inactive Pool", f"{int(current_inactive):,}")

st.markdown("<br>", unsafe_allow_html=True)

# 5. Data Visualization
fig = go.Figure()
fig.add_trace(go.Bar(
    x=df_forecast["Year"], y=df_forecast["Intervention Cost (Billions)"],
    name="Intervention Cost", marker_color='#ef4444'
))
fig.add_trace(go.Scatter(
    x=df_forecast["Year"], y=df_forecast["Net Economic Benefit (Billions)"],
    name="Net GDP Benefit", mode='lines+markers',
    line=dict(color='#22c55e', width=4), marker=dict(size=8)
))

fig.update_layout(
    title="Cost vs. Compound GDP Benefit Analysis",
    xaxis_title="Forecast Year",
    yaxis_title=f"Capital ({curr} Billions)",
    template="plotly_dark", hovermode="x unified",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
st.plotly_chart(fig, use_container_width=True)

# 6. Enterprise Export
st.divider()
csv_export = df_forecast.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Forecasting Model (CSV)",
    data=csv_export,
    file_name=f'{selected_country.lower().replace(" ", "_")}_inactivity_forecast.csv',
    mime='text/csv',
)
