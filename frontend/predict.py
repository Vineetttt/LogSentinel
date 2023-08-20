from io import BytesIO, StringIO
import tempfile
import pdftables_api
import streamlit as st
import requests
import pandas as pd

def highlight(s):
    return ['background-color:rgba(0, 255, 0, 0.1)']*len(s) if s.Compliant else ['background-color: rgba(255,0,0, 0.1)']*len(s)


def load_home_page():
    st.subheader("Base Model: Distilbert-Base-Uncased")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv","txt"])

    # Upload rules from a text file
    rules_file = st.file_uploader("Upload a text file containing rules", type=["txt"])
    if rules_file is not None:
        rules_input = rules_file.read().decode('utf-8')
    else:
        rules_input = ""
    
    if st.button("Predict"):
        if uploaded_file:
            if uploaded_file.type == "text/plain":
                df = pd.read_csv(StringIO(uploaded_file.read().decode('utf-8')), sep='\t')
                converted_file_content = df.to_csv(index=False)
                uploaded_file = converted_file_content

            st.write("Please wait while our model scans your logs for potential threats...")

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
                st.warning(f"There are {count} non-compliant entries in your dataset")
                st.write("After analyzing the logs you provided along with the set of compliance rules our fine-tuned LLM predicts that the following users highlighted in red are non-compliant and can be potential threats to your organization")
                st.write("Please visit the analytics section to gain deeper insights")
                st.subheader("Model Predictions:")

                # Create a DataFrame
                df = pd.DataFrame(original_rows)

                # Apply conditional styling based on 'predicted' attribute
                styled_df = df.style.apply(highlight, axis=1)

                # Display the styled DataFrame
                st.dataframe(styled_df,use_container_width=True) 

            else:
                st.error("Error occurred while predicting.")
        else:
            st.warning("Please upload a CSV file.")