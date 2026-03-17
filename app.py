import streamlit as st
import pandas as pd
import plotly.express as px

### ======================================================
### 1. PAGE CONFIGURATION
### ======================================================
st.set_page_config( page_title="CMIS 2040 Engine", page_icon="🌍", layout="wide", initial_sidebar_state="expanded" )

### ======================================================
### 2. CUSTOM CSS
### ======================================================
st.markdown("""
    <style>
    .main {background-color: #0e1117;}
    h1 {color: #ff4b4b; text-align: center; font-family: 'Arial Black', sans-serif;}
    h3 {color: #faca2b;}
    .stMetric {background-color: #1e2127; padding: 15px; border-radius: 10px; border-left: 5px solid #ff4b4b;}
    </style>
""", unsafe_allow_html=True)

### ======================================================
### 3. TITLE & DEVELOPER NAME
### ======================================================
st.title("🌍 CMIS 2040: Climate Migration Intelligence System")
st.markdown( "<h3>Developed by : Rahul Nayak</h3>", unsafe_allow_html=True )
st.markdown( "<p style='text-align: center; color: #a5a5a5; font-size: 18px;'>" "A Predictive Policy Model for Climate-Induced Migration & Economic Impact in India." "</p>", unsafe_allow_html=True )
st.divider()

### ======================================================
### 4. LOAD DATA
### ======================================================
@st.cache_data 
def load_data(): 
    try: 
        return pd.read_csv('data/CMIS_2040_Ultimate_Predictions.csv') 
    except FileNotFoundError: 
        st.error("Data file not found inside data folder") 
        return pd.DataFrame()

df = load_data()

### ======================================================
### 5. SIDEBAR (PHOTO + OWNER INFO)
### ======================================================
st.sidebar.image( "https://cdn-icons-png.flaticon.com/512/2065/2065064.png", width=100 )
st.sidebar.subheader(" Project Owner")

### 🔥 YOUR PHOTO (LOCAL PATH ADDED HERE)
st.sidebar.image( "rahul.jpg", width=160, caption="Rahul Nayak" )
st.sidebar.divider()

### ======================================================
### 6. SIMULATION CONTROLS
### ======================================================
st.sidebar.header("⚙️ Simulation Engine") 
st.sidebar.markdown("Choose the climate scenario to predict the 2040 impact.")

scenario = st.sidebar.radio( "Select Climate Impact Scenario:", ["🟢 Low Impact", "🟠 Moderate Impact", "🔴 Severe Impact (Extreme Warning)"] )

multiplier = 1.0 
if "Low" in scenario: 
    multiplier = 0.8 
elif "Severe" in scenario: 
    multiplier = 1.6

### ======================================================
### 7. DASHBOARD LOGIC
### ======================================================
if not df.empty:
    # Live recalculations based on user choice
    df['Simulated_Migrants'] = (df['Predicted_Migrants_2040'] * multiplier).astype(int)
    df['Simulated_GDP_Decline'] = df['GDP_Decline_Impact'] * multiplier

    # Top KPI Metrics (Live Changing Numbers)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total Districts Analyzed", value=f"{len(df)}")
    with col2:
        st.metric(label="Total Predicted Migrants", value=f"{df['Simulated_Migrants'].sum():,}", delta=f"{int(df['Simulated_Migrants'].sum() - df['Predicted_Migrants_2040'].sum()):,} from Base")
    with col3:
        highest_danger = df.loc[df['Simulated_Migrants'].idxmax(), 'District']
        st.metric(label="Highest Danger Zone", value=highest_danger)
    with col4:
        avg_gdp_loss = df['Simulated_GDP_Decline'].mean()
        st.metric(label="Avg Rural GDP Decline", value=f"{avg_gdp_loss:.2f}%", delta="Economic Threat", delta_color="inverse")

    st.markdown("<br>", unsafe_allow_html=True)

    # Main Dashboard Visualizations
    col_map, col_charts = st.columns()

    with col_map:
        st.subheader("📍 2040 Migration Threat Map")
        fig_map = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color="Simulated_Migrants",
                                    size="Simulated_Migrants", hover_name="District", 
                                    hover_data=["State", "Climate_Risk_Index", "Simulated_Migrants"],
                                    color_continuous_scale=px.colors.sequential.YlOrRd, size_max=20, zoom=4,
                                    mapbox_style="carto-darkmatter")
        fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="#0e1117")
        st.plotly_chart(fig_map, use_container_width=True)

    with col_charts:
        st.subheader("📊 Top 10 Vulnerable Districts")
        top_10 = df.nlargest(10, 'Simulated_Migrants').sort_values('Simulated_Migrants', ascending=True)
        fig_bar = px.bar(top_10, x='Simulated_Migrants', y='District', text='Simulated_Migrants',
                         color='Simulated_Migrants', color_continuous_scale='Reds', orientation='h')
        fig_bar.update_layout(xaxis_title="Number of Migrants", yaxis_title="", showlegend=False, 
                              paper_bgcolor="#0e1117", font=dict(color='white'))
        st.plotly_chart(fig_bar, use_container_width=True)

    # Secondary Analysis (Risk vs Economy)
    st.divider()
    st.subheader("📈 Climate Risk vs Economic Vulnerability Analysis")
    col_pie, col_scatter = st.columns(2)
    
    with col_pie:
        zone_counts = df['Zone_Name'].value_counts().reset_index()
        zone_counts.columns = ['Zone_Name', 'Count']
        fig_pie = px.pie(zone_counts, values='Count', names='Zone_Name', hole=0.4, 
                         color='Zone_Name', color_discrete_map={'Danger Zone':'red', 'Warning Zone':'orange', 'Safe Zone':'green'})
        fig_pie.update_layout(paper_bgcolor="#0e1117", font=dict(color='white'))
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col_scatter:
        fig_scatter = px.scatter(df, x='Climate_Risk_Index', y='Simulated_GDP_Decline', color='Zone_Name',
                                 size='Population', hover_name='District',
                                 color_discrete_map={'Danger Zone':'red', 'Warning Zone':'orange', 'Safe Zone':'green'})
        fig_scatter.update_layout(xaxis_title="Climate Risk Index", yaxis_title="GDP Decline (%)", 
                                  paper_bgcolor="#0e1117", font=dict(color='white'))
        st.plotly_chart(fig_scatter, use_container_width=True)

    st.sidebar.divider()
    st.sidebar.info("💡 Project Status: Live 🟢\nEngineered for 2040 Policymaking")
