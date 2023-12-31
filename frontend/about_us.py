import streamlit as st

def load_about():
    st.markdown("Empower your business with intelligent log analysis and compliance monitoring.")

    st.header("Description")
    st.markdown("The Compliance Monitoring and Log Analysis Platform is an innovative solution designed to empower businesses with the ability to ensure compliance, detect potential threats, and gain deep insights from their log data. This platform leverages cutting-edge technologies, including large language models and data analytics, to provide a comprehensive approach to log analysis and security monitoring.")
    
    st.header("Key Features")
    st.markdown("• Fine-tuned open source DistilBERT LLM for performing RTE based on the set of rules provided along with the log data.")
    st.markdown("• Ability of the system to handle various input formats (txt,csv) for log data and rules.")
    st.markdown("• Powerful dashboard providing deeper insights into the log data for monitoring.")
    st.markdown("• Smooth and intuitive UI for users to interact with the system.")
    st.markdown("• High Accuracy averaging to 96% with very low false positives and false negatives.")
    st.markdown("• Notable performance with around 1.5 minutes being taken to make predictions on over 100 log entries.")
    

    # Expandable section for uploading logs
    with st.expander("Uploading Logs"):
        st.write("To upload logs, follow these steps:")
        st.write("1. Click on the 'Predict Compliance' section.")
        st.write("2. Use the 'Upload a CSV file' button to select your log file.")
        st.write("3. You can also upload rules from a text file using the 'Upload a text file containing rules' button.")
        st.write("4. Click the 'Predict' button to analyze the logs.")
    
    
    st.markdown("Project by:")
    st.markdown("Vineet Chotaliya")
    st.markdown("B.Tech CSE DS - 2025")
    st.markdown("Shri Vile Parle Kelavani Mandal's Dwarkadas J. Sanghvi College of Engineering (DJSCE), Mumbai")

    st.write("If you have any questions or inquiries, please feel free to contact us:")
    st.write("- Email: vineetchotaliya30@gmail.com")
    st.write("- Phone: +91 9326674067")
    st.write("Stay connected with us on social media:")
    st.write("- Github: [@Vineetttt](https://github.com/Vineetttt)")
    st.write("- LinkedIn: [Vineet Chotaliya](https://www.linkedin.com/in/vineet-chotaliya-015238246/)")