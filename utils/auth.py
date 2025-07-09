import streamlit as st

def login_form():
    st.subheader("🔐 Login to MoodMate")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state.authenticated = True
            st.success(f"Welcome, {username.split('@')[0]}!")
        else:
            st.error("Invalid credentials.")

def authenticate_user(username, password):
    return st.secrets["credentials"].get(username) == password
