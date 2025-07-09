import streamlit as st

def therapy_bot_page():
    st.subheader("🧠 Therapy Bot – CBT Reflection")
    
    st.markdown("Let's go through a quick CBT session. Please respond honestly.")

    prompts = [
        "What negative thought crossed your mind recently?",
        "What evidence supports this thought?",
        "What evidence contradicts it?",
        "What's a more balanced way to think about it?",
        "How do you feel now (emotionally & physically)?"
    ]

    for i, prompt in enumerate(prompts):
        st.text_input(f"{i+1}. {prompt}", key=f"cbt_{i}")
    
    if st.button("💡 Reflect & Save"):
        st.success("Your responses have been saved privately. Try to revisit them later.")
