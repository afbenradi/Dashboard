import streamlit as st
import pandas as pd
import plotly.express as px

# Configuration de la page
st.set_page_config(page_title="Test Streamlit", layout="wide")

# Titre de l'application
st.title("Tableau de Bord Test - Streamlit")

# Chargement de données fictives
@st.cache_data
def load_data():
    # Exemple de données fictives
    data = pd.DataFrame({
        "Employee": ["A", "B", "C", "D", "E"],
        "Satisfaction": [0.8, 0.6, 0.4, 0.9, 0.7],
        "Turnover": [0, 1, 1, 0, 0],
        "Monthly_Hours": [160, 200, 250, 150, 180],
        "Salary": ["High", "Low", "Medium", "High", "Low"]
    })
    return data

# Chargement des données
data = load_data()

# Affichage des données
st.subheader("Aperçu des Données")
st.dataframe(data)

# KPI Exemple
turnover_rate = data["Turnover"].mean() * 100
avg_satisfaction = data["Satisfaction"].mean()

col1, col2 = st.columns(2)
col1.metric("Taux de Turnover (%)", f"{turnover_rate:.1f}")
col2.metric("Satisfaction Moyenne", f"{avg_satisfaction:.2f}")

# Graphique interactif - Exemple avec Plotly
st.subheader("Graphique de Satisfaction")
fig = px.bar(
    data,
    x="Employee",
    y="Satisfaction",
    title="Niveau de Satisfaction par Employé",
    labels={"Satisfaction": "Niveau de Satisfaction", "Employee": "Employé"},
    text="Satisfaction"
)
st.plotly_chart(fig, use_container_width=True)

# Scatter Plot - Satisfaction vs Heures Mensuelles
st.subheader("Satisfaction vs Heures Mensuelles")
fig_scatter = px.scatter(
    data,
    x="Monthly_Hours",
    y="Satisfaction",
    color="Salary",
    title="Satisfaction vs Heures Mensuelles (par Niveau de Salaire)",
    labels={"Monthly_Hours": "Heures Mensuelles", "Satisfaction": "Satisfaction"}
)
st.plotly_chart(fig_scatter, use_container_width=True)