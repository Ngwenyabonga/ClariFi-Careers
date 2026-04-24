import streamlit as st
import openai
import os

# Set up OpenAI API key from Streamlit secrets
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Create top tab navigation
tab1, tab2, tab3, tab4 = st.tabs(["CV Review", "AI Coach", "Learning Hub", "Fun Corner"])

# --- CV REVIEW TAB ---
with tab1:
    st.header("Get Your CV Reviewed")
    st.write("Upload OR paste your CV and get honest, specific feedback — like having a senior hiring manager read your CV over coffee.")

    # Upload option
    uploaded_file = st.file_uploader("Upload CV File", type=["pdf", "docx"])

    # Paste option
    cv_text = st.text_area("Paste CV Text")

    # Decide which input to use
    if uploaded_file is not None:
        cv_text = uploaded_file.read().decode("utf-8", errors="ignore")

    if st.button("Review My CV"):
        if cv_text:
            # Build recruiter-style prompt
            prompt = f"""
You are a senior recruitment consultant and career branding expert with 15+ years of experience screening CVs.

A candidate has submitted their CV. Here is the full text:

---
{cv_text}
---

Your task:
1. Extract the candidate's FULL NAME from the CV.
2. Identify their most recent or highest-level job title.
3. Analyse the CV thoroughly and identify exactly 6–8 specific, constructive issues. These must be SPECIFIC to THIS candidate's CV — not generic advice. Reference actual sections, wording, or gaps you see.

Respond in EXACTLY this format:

"Thank you for sharing your CV, [Candidate Full Name].

I'll be very direct, speaking as someone who's reviewed [their most recent job title/seniority level] CVs for over 10 years:

- [Issue 1 — specific to their CV content]
- [Issue 2]
- [Issue 3]
- [Issue 4]
- [Issue 5]
- [Issue 6]

In short: your experience may be strong, but the presentation is actively working against you and will get this CV rejected before it’s read."
"""

            # Call the OpenAI model
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            feedback = response.choices[0].message.content
            st.markdown(feedback)
        else:
            st.warning("⚠️ Please upload or paste your CV first.")

# --- AI COACH TAB ---
with tab2:
    st.header("AI Coach")
    st.write("This will be your interactive career coach. (Chat features coming soon.)")

# --- LEARNING HUB TAB ---
with tab3:
    st.header("Learning Hub")
    st.write("Access guides, templates, and resources here.")

# --- FUN CORNER TAB ---
with tab4:
    st.header("Fun Corner")
    st.write("Relax with light content, jokes, or games.")
