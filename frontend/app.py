import streamlit as st
import pandas as pd
from home import load_home_page
from dashboard import load_dashboard

# Streamlit app
st.set_page_config(
    page_title="Compliance Monitoring",
    page_icon="🕵️‍♂️",
    layout="wide"
)


# Streamlit app
st.title("Compliance Monitoring")

# Sidebar for selecting APIs
st.sidebar.header("LogAnalyzer")
selected_api = st.sidebar.radio("", ["MONITOR YOUR LOGS","DASHBOARD"])

# Predict CSV UI
if selected_api == "MONITOR YOUR LOGS":
    load_home_page()
elif selected_api == "DASHBOARD":
    load_dashboard()