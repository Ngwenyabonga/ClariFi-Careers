import streamlit as st

# Create top tab navigation
tab1, tab2, tab3, tab4 = st.tabs(["CV Review", "AI Coach", "Learning Hub", "Fun Corner"])

# --- CV REVIEW TAB ---
with tab1:
    st.header("Get Your CV Reviewed")
    st.write("Upload or paste your CV and get honest, specific feedback — like having a senior hiring manager read your CV over coffee.")

    # Upload option
    uploaded_file = st.file_uploader("Upload CV File", type=["pdf", "docx"])

    # Paste option
    cv_text = st.text_area("Paste CV Text")

    # Simple feedback simulation
    if uploaded_file or cv_text:
        st.success("✅ Your CV has been received! Feedback will be generated here.")
        st.write("Tip: Make sure your CV highlights achievements, not just duties.")

# --- AI COACH TAB ---
with tab2:
    st.header("AI Coach")
    st.write("This will be your interactive career coach. (We’ll add chat features here next.)")

# --- LEARNING HUB TAB ---
with tab3:
    st.header("Learning Hub")
    st.write("Access guides, templates, and resources here.")

# --- FUN CORNER TAB ---
with tab4:
    st.header("Fun Corner")
    st.write("Relax with light content, jokes, or games.")
