import streamlit as st
import requests
import pandas as pd

st.title("CSV Predictor App")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    st.write("File uploaded successfully!")
    st.write("Predicting...")

    # Make API request
    url = "http://localhost:4000/predict_csv"
    files = {'fisier': uploaded_file}
    response = requests.post(url, files=files)

    if response.status_code == 200:
        data = response.json()
        filtered_rows = data['filtered_rows']
        count = data['count']

        # Display results
        st.write(f"Filtered Rows Count: {count}")
        st.write("Filtered Rows:")
        df = pd.DataFrame(filtered_rows)
        st.dataframe(df)
    else:
        st.write("Error occurred while predicting.")
