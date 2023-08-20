from io import StringIO
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def highlight(s):
    return ['background-color: rgba(255,0,0, 0.1)']*len(s)

def load_dashboard():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("Analytics Dashboard")

    # Upload CSV file for analysis
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv","txt"])

    if uploaded_file:
        st.subheader("Uploaded Data")
        data = pd.read_csv(uploaded_file)
        st.dataframe(data)

        st.subheader("Non-Compliant Users")
    
        non_compliant_users = data[data['Compliant'] == 0]['UserID'].unique()
        non_compliant_df = pd.DataFrame({'UserID': non_compliant_users, 'Action': ["BLOCK  INSPECT  REVOKE"] * len(non_compliant_users)})
        non_compliant_df = non_compliant_df.style.apply(highlight,axis=1)
        
        # Display the DataFrame with the button
        st.dataframe(non_compliant_df, width=300,hide_index=True,)

        st.subheader("Insights")

        # User Type Distribution and Request Type Analysis
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("User Type Distribution")
            user_type_counts = data['User Type'].value_counts()
            st.bar_chart(user_type_counts, width=300)

        with col2:
            st.subheader("Compliance vs. Non-Compliance")
            compliance_counts = data['Compliant'].value_counts()
            st.bar_chart(compliance_counts, width=300)


        # Compliance vs. Non-Compliance and Endpoint Usage
        col3, col4 = st.columns(2)

        with col3:
            st.subheader("Request Type Analysis")
            request_type_counts = data['Request Type'].value_counts()
            fig, ax = plt.subplots()
            ax.pie(request_type_counts, labels=request_type_counts.index, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
            st.pyplot(fig)

        with col4:
            st.subheader("Endpoint Usage")
            endpoint_counts = data['Endpoint'].value_counts().head(10)
            st.bar_chart(endpoint_counts, width=300)

        col5, col6 = st.columns(2)
        with col5:
            st.subheader("Endpoint Analysis by Compliance")
            endpoint_compliance = data.groupby(['Endpoint', 'Compliant']).size().unstack()
            endpoint_compliance.plot(kind='barh', stacked=True, figsize=(10, 6))
            plt.xlabel("Count")
            plt.ylabel("Endpoint")
            plt.title("Endpoint Analysis by Compliance")
            st.pyplot()

        with col6:
            st.subheader("Hourly Request Distribution")
            data['Timestamp'] = pd.to_datetime(data['Timestamp'])
            data['Hour'] = data['Timestamp'].dt.hour

            hourly_distribution = data['Hour'].value_counts().sort_index()
            st.line_chart(hourly_distribution, use_container_width=True)

        # Calculate Total Number of Requests
        total_requests = len(data)
        compliant_percentage = (data['Compliant'].sum() / total_requests) * 100
        busiest_user_agent = data['User Agent'].value_counts().idxmax()
        average_response_time_compliant = data[data['Compliant']]['Response Time'].mean()
        average_response_time_non_compliant = data[~data['Compliant']]['Response Time'].mean()

        insights_df = pd.DataFrame({
            "Insight": ["Total Number of Requests", "Percentage of Compliant Requests",
                        "Busiest User Agent", "Avg Response Time - Compliant",
                        "Avg Response Time - Non-Compliant"],
            "Value": [total_requests, f"{compliant_percentage:.2f}%",
                      busiest_user_agent, f"{average_response_time_compliant:.2f} ms",
                      f"{average_response_time_non_compliant:.2f} ms"]
        })

        st.dataframe(insights_df)
