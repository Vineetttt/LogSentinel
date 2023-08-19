import streamlit as st
import requests
import pandas as pd

# Streamlit app
st.title("API Demo")

# Sidebar for selecting APIs
selected_api = st.sidebar.radio("Select API", ["Predict CSV"])

# Predict CSV UI
if selected_api == "Predict CSV":
    st.subheader("CSV Predictor App")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    # Rules input
    rules_input = st.text_area("Enter rules (one rule per line)")

    if st.button("Predict"):
        if uploaded_file and rules_input:
            st.write("Predicting...")

            # Prepare file data to be sent to the API
            files = {'file': uploaded_file}
            data = {'rules': rules_input}

            # Make API request
            url = "http://localhost:4000/api/v1/predict_csv"
            response = requests.post(url, files=files, data=data)

            if response.status_code == 200:
                data = response.json()
                original_rows = data['filtered_rows']  # Update variable name
                count = data['count']  # Update variable name

                # Display results
                st.write(f"Filtered Rows Count: {count}")  # Update variable name
                st.write("Filtered Rows:")
                df = pd.DataFrame(original_rows)
                st.dataframe(df)
            else:
                st.write("Error occurred while predicting.")

        else:
            st.write("Please upload a CSV file and enter rules.")