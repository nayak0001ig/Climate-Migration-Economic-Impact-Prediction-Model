# CMIS 2040: Climate Migration Intelligence System

A comprehensive predictive intelligence platform analyzing climate-induced migration patterns in India through 2040.

## 📊 Project Overview

This project combines climate data analysis, socioeconomic vulnerability assessment, and machine learning to predict migration threats and economic impacts across Indian districts.

## 🎯 Key Features

- **Climate Risk Analysis**: Temperature, AQI, and rainfall impact modeling
- **Socio-Economic Vulnerability Index**: Combines literacy rates and employment data
- **Migration Threat Scoring**: Integrated risk assessment across 20+ districts
- **ML Predictions**: Random Forest regression for 2040 migration rate forecasting
- **Interactive Dashboard**: Streamlit-powered visualization and scenario simulation
- **Scenario Planning**: Low/Moderate/Severe climate impact simulations

## 📁 Project Structure

```
CMIS_2040/
├── app.py                                    # Streamlit dashboard application
├── notebooks/
│   └── data_cleaning_eda.ipynb              # Data exploration & ML pipeline
├── data/
│   ├── Indian_Climate_Dataset_2024_2025.csv # Climate observations
│   ├── India (1).csv                        # Demographics data
│   ├── CMIS_Dashboard_Data.csv              # Processed dashboard dataset
│   └── CMIS_2040_Ultimate_Predictions.csv   # Final predictions with all metrics
├── .gitignore
└── README.md
```

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/CMIS_2040.git
cd CMIS_2040

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows

# Install dependencies
pip install streamlit pandas plotly scikit-learn jupyter matplotlib seaborn
```

### Run Dashboard

```bash
streamlit run app.py
```

Access at: `http://localhost:8501`

### Run Analysis Notebook

```bash
jupyter notebook notebooks/data_cleaning_eda.ipynb
```

## 📊 Dashboard Features

- **2040 Migration Threat Map**: Geospatial visualization with Mapbox
- **Top 10 Vulnerable Districts**: Bar chart highlighting highest impact zones
- **Zone Classification**: Safe/Warning/Danger zones via K-Means clustering
- **Risk vs Economy Analysis**: Scatter plots showing climate-economic relationships
- **Interactive Scenarios**: Switch between Low/Moderate/Severe climate impact projections

## 🔬 ML Model Details

**Algorithm**: Random Forest Regressor (200 estimators)
- **Features**: Temperature_Max, AQI, Rainfall, Socio_Econ_Vulnerability, Climate_Risk_Index
- **Target**: Future_Migration_Rate_2040_pct
- **Model Accuracy**: ~[R² Score]% (See dashboard for live results)

## 📈 Key Metrics

- **Total Districts Analyzed**: 600+
- **Baseline Migrants (2040)**: 200M+ 
- **Economic Impact**: -1.2% GDP decline per migration %

## 📊 Data Sources

- Indian Climate Dataset (2024-2025)
- India Demographics Census Data
- Population & Socioeconomic Indicators

## 🛠️ Technologies Used

- **Python 3.13**
- **Streamlit**: Interactive web dashboard
- **Pandas**: Data manipulation
- **Scikit-learn**: ML pipeline
- **Plotly**: Interactive visualizations
- **Jupyter**: Data exploration

## 📝 License

MIT License - feel free to use this project for research and policy analysis.

## 👤 Author

Developed for CMIS 2040 Climate Migration Intelligence initiative.

---

*"Predicting Climate Futures, Planning Migration Solutions"* 🌍
