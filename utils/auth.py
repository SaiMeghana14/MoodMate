import streamlit as st
import pyrebase

firebase_config = {
    "apiKey": st.secrets["pyrebase"]["apiKey"],
    "authDomain": st.secrets["pyrebase"]["authDomain"],
    "projectId": st.secrets["pyrebase"]["projectId"],
    "databaseURL": st.secrets["pyrebase"]["databaseURL"],
    "storageBucket": st.secrets["pyrebase"]["storageBucket"],
    "messagingSenderId": st.secrets["pyrebase"]["messagingSenderId"],
    "appId": st.secrets["pyrebase"]["appId"]
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()

def login_form():
    st.sidebar.header("🔐 Login / Signup")
    choice = st.sidebar.selectbox("Action", ["Login", "Sign Up"])
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Submit"):
        try:
            if choice == "Login":
                user = auth.sign_in_with_email_and_password(email, password)
            else:
                user = auth.create_user_with_email_and_password(email, password)
            st.success(f"Logged in as {email}")
            st.session_state["uid"] = user["localId"]
            st.session_state["email"] = email
            st.session_state["db"] = db
        except Exception as e:
            st.error("Authentication Failed. Please check your credentials.")

def authenticate_user():
    return st.session_state.get("uid", None)
