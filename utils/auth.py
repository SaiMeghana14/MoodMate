import streamlit as st
import json
import os

USERS_FILE = "users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def login_form():
    st.subheader("🔐 Login to MoodMate")
    users = load_users()
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login", key="login_btn"):
        if username in users and users[username]["password"] == password:
            st.success("✅ Login successful!")
            st.session_state.user = username
            return True
        else:
            st.error("Invalid credentials.")
    return False

def signup_form():
    st.subheader("📝 Create a MoodMate Account")
    users = load_users()
    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type="password")
    if st.button("Signup", key="signup_btn"):
        if username in users:
            st.warning("Username already exists.")
        else:
            users[username] = {"password": password, "journals": {}, "streak": 0}
            save_users(users)
            st.success("Account created! Please log in.")
