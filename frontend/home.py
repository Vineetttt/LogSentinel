import streamlit as st
import requests
import pandas as pd

def highlight_survived(s):
    return ['background-color:rgba(0, 255, 0, 0.1)']*len(s) if s.Compliant else ['background-color: rgba(255,0,0, 0.1)']*len(s)

def color_survived(val):
    color = 'rgba(0, 255, 0, 0.1)' if val else ' rgba(255, 0, 0, 0.1)'
    return f'background-color: {color}'

def load_home_page():
    st.subheader("Base Model: Distilbert-Base-Uncased")

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
                original_rows = data['filtered_rows']
                count = data['count']

                # Display results
                st.warning(f"There are {count} non compliant entries in your dataset")
                st.write("Please visit analytics section to gain deeper insights")
                st.subheader("Analysis:")
                df = pd.DataFrame(original_rows)

                # Apply conditional styling based on 'compliant' attribute
                styled_df = df.style.apply(highlight_survived, axis=1)
                st.dataframe(styled_df)
            else:
                st.error("Error occurred while predicting.")

        else:
            st.warning("Please upload a CSV file and enter rules.")