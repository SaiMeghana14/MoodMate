# Email-password based login using Streamlit + Firebase
import streamlit as st
import pyrebase

firebase_config = dict(st.secrets["firebase"])
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def login_form():
    st.sidebar.subheader("🔐 Login to MoodMate")
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.session_state["uid"] = user["localId"]
            st.session_state["email"] = email
            st.success("✅ Logged in!")
        except:
            st.error("❌ Login failed. Please check credentials.")

    if st.sidebar.button("Sign Up"):
        try:
            user = auth.create_user_with_email_and_password(email, password)
            st.success("✅ Account created. Please login.")
        except:
            st.error("⚠️ Account already exists or invalid.")

def authenticate_user():
    return st.session_state.get("uid", None)
