import streamlit as st
import firebase_admin
from firebase_admin import auth, credentials

# Firebase Admin should already be initialized in app.py
def get_user_id_by_email(email):
    try:
        user = auth.get_user_by_email(email)
        return user.uid
    except:
        return None

def signup_user(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        return user.uid
    except Exception as e:
        st.error(f"❌ Signup failed: {e}")
        return None

def login_form():
    st.sidebar.header("🔐 Login / Signup")
    mode = st.sidebar.radio("Select Mode", ["Login", "Signup"])
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")
    login_btn = st.sidebar.button("Submit")

    if login_btn and email and password:
        if mode == "Signup":
            uid = signup_user(email, password)
            if uid:
                st.success("✅ Signup successful!")
                st.session_state["uid"] = uid
                st.session_state["email"] = email
        else:
            uid = get_user_id_by_email(email)
            if uid:
                st.success("✅ Login successful!")
                st.session_state["uid"] = uid
                st.session_state["email"] = email
            else:
                st.error("❌ Invalid credentials or user not found")
