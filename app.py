import streamlit as st
import pandas as pd
import plotly.express as px

# ======================================================
# 1. PAGE CONFIGURATION
# ======================================================
st.set_page_config(
    page_title="CMIS 2040 Engine",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================
# 2. CUSTOM CSS
# ======================================================
st.markdown("""
<style>
.main {background-color: #0e1117;}
h1 {color: #ff4b4b; text-align: center; font-family: 'Arial Black', sans-serif;}
h3 {color: #4fd1c5; text-align: center;}
.stMetric {
    background-color: #1e2127;
    padding: 15px;
    border-radius: 10px;
    border-left: 5px solid #ff4b4b;
}
</style>
""", unsafe_allow_html=True)

# ======================================================
# 3. TITLE & DEVELOPER NAME
# ======================================================
st.title("🌍 CMIS 2040: Climate Migration Intelligence System")

st.markdown(
    "<h3>Developed by: Rahul Nayak</h3>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: #a5a5a5; font-size: 18px;'>"
    "A Predictive Policy Model for Climate-Induced Migration & Economic Impact in India."
    "</p>",
    unsafe_allow_html=True
)

st.divider()

# ======================================================
# 4. LOAD DATA
# ======================================================
@st.cache_data
def load_data():
    try:
        return pd.read_csv('data/CMIS_2040_Ultimate_Predictions.csv')
    except FileNotFoundError:
        st.error("Data file not found inside data folder")
        return pd.DataFrame()

df = load_data()

# ======================================================
# 5. SIDEBAR (PHOTO + OWNER INFO)
# ======================================================
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2065/2065064.png",
    width=100
)

st.sidebar.subheader(" Project Owner")

# 🔥 YOUR PHOTO (LOCAL PATH ADDED HERE)
st.sidebar.image(
    "C:/Users/nayak/OneDrive/Desktop/CMIS_2040_Project/rahul.jpg",
    width=160,
    caption="Rahul Nayak"
)

st.sidebar.divider()

# ======================================================
# 6. SIMULATION CONTROLS
# ======================================================
st.sidebar.header("⚙️ Simulation Engine")
st.sidebar.markdown("Choose the climate scenario to predict the 2040 impact.")

scenario = st.sidebar.radio(
    "Select Climate Impact Scenario:",
    ["🟢 Low Impact", "🟠 Moderate Impact", "🔴 Severe Impact (Extreme Warning)"]
)

multiplier = 1.0
if "Low" in scenario:
    multiplier = 0.8
elif "Severe" in scenario:
    multiplier = 1.6

# ======================================================
# 7. DASHBOARD LOGIC
# ======================================================
if not df.empty:

    df['Simulated_Migrants'] = (df['Predicted_Migrants_2040'] * multiplier).astype(int)
    df['Simulated_GDP_Decline'] = df['GDP_Decline_Impact'] * multiplier

    # KPI METRICS
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Districts Analyzed", len(df))

    with col2:
        st.metric(
            "Total Predicted Migrants",
            f"{df['Simulated_Migrants'].sum():,}",
            delta=f"{int(df['Simulated_Migrants'].sum() - df['Predicted_Migrants_2040'].sum()):,} from Base"
        )

    with col3:
        danger = df.loc[df['Simulated_Migrants'].idxmax(), 'District']
        st.metric("Highest Danger Zone", danger)

    with col4:
        st.metric(
            "Avg Rural GDP Decline",
            f"{df['Simulated_GDP_Decline'].mean():.2f}%",
            delta="Economic Threat",
            delta_color="inverse"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # MAP + BAR CHART
    col_map, col_chart = st.columns([3, 4])

    with col_map:
        st.subheader("📍 2040 Migration Threat Map")
        fig_map = px.scatter_mapbox(
            df,
            lat="Latitude",
            lon="Longitude",
            size="Simulated_Migrants",
            color="Simulated_Migrants",
            hover_name="District",
            hover_data=["State", "Climate_Risk_Index"],
            color_continuous_scale="YlOrRd",
            size_max=20,
            zoom=4,
            mapbox_style="carto-darkmatter"
        )
        fig_map.update_layout(margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig_map, use_container_width=True)

    with col_chart:
        st.subheader("📊 Top 10 Vulnerable Districts")
        top10 = df.nlargest(10, "Simulated_Migrants").sort_values("Simulated_Migrants")
        fig_bar = px.bar(
            top10,
            x="Simulated_Migrants",
            y="District",
            orientation="h",
            color="Simulated_Migrants",
            text="Simulated_Migrants",
            color_continuous_scale="Reds"
        )
        fig_bar.update_layout(showlegend=False)
        st.plotly_chart(fig_bar, use_container_width=True)

    # SECONDARY ANALYSIS
    st.divider()
    st.subheader("📈 Climate Risk vs Economic Vulnerability")

    col_pie, col_scatter = st.columns(2)

    with col_pie:
        zone_data = df['Zone_Name'].value_counts().reset_index()
        zone_data.columns = ['Zone', 'Count']
        fig_pie = px.pie(zone_data, values="Count", names="Zone", hole=0.4)
        st.plotly_chart(fig_pie, use_container_width=True)

    with col_scatter:
        fig_scatter = px.scatter(
            df,
            x="Climate_Risk_Index",
            y="Simulated_GDP_Decline",
            size="Population",
            color="Zone_Name",
            hover_name="District"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

st.sidebar.divider()
st.sidebar.info("💡 Project Status: Live 🟢\nEngineered for 2040 Policymaking")