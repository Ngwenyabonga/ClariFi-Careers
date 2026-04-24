import streamlit as st

# Create top tab navigation
tab1, tab2, tab3, tab4 = st.tabs(["CV Review", "AI Coach", "Learning Hub", "Fun Corner"])

# --- CV REVIEW TAB ---
with tab1:
    st.header("Get Your CV Reviewed")
    st.write("Upload or paste your CV and get honest, specific feedback — like having a senior hiring manager read your CV over coffee.")

    # Upload option
    uploaded_file = st.file_uploader("Upload CV File", type=["pdf", "docx"])
    cv_text = st.text_area("Paste CV Text")

    # Button to trigger review
    if st.button("Review My CV"):
        if uploaded_file:
            st.info("📂 File uploaded. (For now, feedback will be based on pasted text.)")
        if cv_text:
            # Simulated AI feedback
            st.success(f"✅ Thank you for sharing your CV.")
            st.markdown(f"""
**Direct Feedback:**

- Your CV is too long — try cutting it down to 2 pages.
- Your achievements are hidden in duties. Highlight measurable results.
- Your formatting is inconsistent (fonts, spacing).
- Your most recent role needs clearer responsibilities.
- Your education section is buried — bring it forward.
- Your contact details are missing LinkedIn — recruiters expect it.

To be honest, this isn't just a content problem. It's a positioning and structure problem.
            """)
        else:
            st.warning("⚠️ Please upload or paste your CV first.")

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
