
import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Quantum Wi-Fi Localization Dashboard", layout="wide")

st.markdown(
    '<h1 style="text-align:center; color:#00FFFF; font-size:45px;">🌐 Quantum Wi-Fi Localization Dashboard</h1>',
    unsafe_allow_html=True
)
st.markdown("<p style='text-align:center; color:gray;'>Made by <b>Somu Rohit – RA2211003010219</b></p>", unsafe_allow_html=True)

st.sidebar.success("Select a page from the navigation bar 👇")

st.image("assets/logo.png", width=150)

st.markdown("""
Welcome to the **Quantum Wi-Fi Localization Dashboard** — a visualization of how Quantum Machine Learning
(QSVC, VQC, QNN) performs on Wi-Fi signal localization tasks using real data.
""")

# Quick Metrics
st.subheader("📊 Model Performance Summary")
data = {
    "Quantum Model": ["QSVC", "VQC", "QNN"],
    "Accuracy": [0.390, 0.625, 0.667]
}
df = pd.DataFrame(data)
fig = px.bar(df, x="Quantum Model", y="Accuracy", color="Quantum Model",
             color_discrete_sequence=px.colors.sequential.Aggrnyl,
             text="Accuracy", title="Quantum Model Accuracy Comparison")
st.plotly_chart(fig, use_container_width=True)

st.markdown("<hr style='border: 1px solid #00FFFF;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00FFFF;'>Quantum Localization Dashboard © 2025 – Somu Rohit</p>", unsafe_allow_html=True)
