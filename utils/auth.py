import streamlit as st

def user_login():
    st.sidebar.title("🔐 Login")
    email = st.sidebar.text_input("Enter your email to proceed", key="email_input")
    if email:
        st.sidebar.success(f"Logged in as: {email}")
        return email
    else:
        st.sidebar.warning("Please enter your email to use the app.")
        return None
