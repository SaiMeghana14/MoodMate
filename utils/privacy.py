import streamlit as st

def privacy_settings_page():
    st.subheader("🔐 Privacy Settings")

    storage_mode = st.radio("Choose storage option:", ["Cloud Sync", "Local-Only (No Upload)"])
    st.success(f"Current Mode: {storage_mode}")

    st.markdown("### 🗂️ Data Management")
    if st.button("📥 Export My Data"):
        st.info("Your data has been packaged for export (mockup).")
    if st.button("🗑️ Delete My Data"):
        st.warning("Your journal & chatbot history has been cleared (mockup).")
