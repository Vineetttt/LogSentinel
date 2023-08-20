import streamlit as st
import pandas as pd
from predict import load_home_page
from dashboard import load_dashboard
from about_us import load_about
import streamlit_authenticator as stauth
import pickle
from pathlib import Path

st.set_page_config(page_title="Compliance Monitoring", page_icon="🕵️‍♂️")

names = ['Vineet Chotaliya','Test User']
usernames = ['vineet','test@123']
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

credentials = {
        "usernames":{
            usernames[0]:{
                "name":names[0],
                "password":hashed_passwords[0]
                },
            usernames[1]:{
                "name":names[1],
                "password":hashed_passwords[1]
                }            
            }
}

authenticator = stauth.Authenticate(credentials,'compliance_monitoring','abcde')
name, authentication_status, username = authenticator.login('Login', 'main')
        
if authentication_status == True:
    st.title("LogSentinel")
    st.title("Compliance Monitoring and Log Analysis Platform")
    st.sidebar.header("LogSentinel")
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
    selected_api = st.sidebar.radio("", ["About Us","Predict Compliance","Dashboard"])
    if selected_api == "Predict Compliance":
        load_home_page()
    elif selected_api == "Dashboard":
        load_dashboard()
    elif selected_api == "About Us":
        load_about()
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
