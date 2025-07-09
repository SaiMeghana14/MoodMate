import streamlit as st
import pyrebase

# Firebase Config - Loaded from Streamlit secrets
firebase_config = st.secrets["firebase"]

# Initialize Firebase app
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()

# Save db to session state for reuse
st.session_state["db"] = db

# ----------------------------
# 🔐 Login / Signup Form
# ----------------------------
def login_form():
    st.sidebar.title("🔐 Login / Signup")

    mode = st.sidebar.radio("Choose Mode", ["Login", "Signup"])

    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")

    if mode == "Signup":
        if st.sidebar.button("Create Account"):
            try:
                user = auth.create_user_with_email_and_password(email, password)
                st.success("✅ Account created successfully! Please login.")
            except Exception as e:
                st.error(f"Signup failed: {e}")
    else:
        if st.sidebar.button("Login"):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state["uid"] = user["localId"]
                st.session_state["email"] = email
                st.session_state["token"] = user["idToken"]
                st.rerun()
            except Exception as e:
                st.error(f"Login failed: {e}")

# ----------------------------
# ✅ Check if Authenticated
# ----------------------------
def authenticate_user():
    return st.session_state.get("uid", None)
