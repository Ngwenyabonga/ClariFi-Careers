import streamlit as st
import openai

# Get API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Top tab navigation
tab1, tab2, tab3, tab4 = st.tabs(["CV Review", "AI Coach", "Learning Hub", "Fun Corner"])

# --- CV REVIEW TAB ---
with tab1:
    st.header("Get Your CV Reviewed")
    st.write("Upload OR paste your CV and get honest, specific feedback.")

    uploaded_file = st.file_uploader("Upload CV File", type=["pdf", "docx"])
    cv_text = st.text_area("Paste CV Text")

    # If user uploads, read file
    if uploaded_file is not None:
        try:
            cv_text = uploaded_file.read().decode("utf-8", errors="ignore")
        except Exception:
            st.error("⚠️ Could not read file. Please paste text instead.")

    if st.button("Review My CV"):
        if cv_text:
            prompt = f"""
You are a senior recruitment consultant with 15+ years of experience screening CVs.

Here is the candidate's CV:

---
{cv_text}
---

Your task:
1. Extract the candidate's FULL NAME.
2. Identify their most recent or highest-level job title.
3. Analyse the CV thoroughly and identify 6–8 specific issues, referencing actual wording or gaps.

Respond in this format:

"Thank you for sharing your CV, [Candidate Full Name].

I'll be very direct, speaking as someone who's reviewed [their most recent job title/seniority level] CVs for over 10 years:

- [Issue 1 — specific to their CV]
- [Issue 2]
- [Issue 3]
- [Issue 4]
- [Issue 5]
- [Issue 6]

In short: your experience may be strong, but the presentation is actively working against you and will get this CV rejected before it’s read."
"""

            try:
                response = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}]
                )
                feedback = response.choices[0].message.content
                st.markdown(feedback)
            except Exception as e:
                st.error(f"⚠️ Error generating feedback: {e}")
        else:
            st.warning("⚠️ Please upload or paste your CV first.")

# --- Other Tabs ---
with tab2:
    st.header("AI Coach")
    st.write("Interactive career coach coming soon.")

with tab3:
    st.header("Learning Hub")
    st.write("Guides and resources here.")

with tab4:
    st.header("Fun Corner")
    st.write("Relax with light content.")
