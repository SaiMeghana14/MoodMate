# utils/auth.py
import streamlit as st
import pyrebase

firebase_config = dict(st.secrets["firebase"])
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()

def login_form():
    st.sidebar.title("🔐 Login to MoodMate")

    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")
    
    if st.sidebar.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.session_state["uid"] = user["localId"]
            st.session_state["email"] = email
            st.session_state["db"] = db
            st.sidebar.success("✅ Logged in!")
        except:
            st.sidebar.error("❌ Login failed. Please check credentials.")
    
    if st.sidebar.button("Sign Up"):
        try:
            user = auth.create_user_with_email_and_password(email, password)
            st.sidebar.success("✅ Account created. You can now log in.")
        except:
            st.sidebar.error("⚠️ Account already exists or invalid.")
