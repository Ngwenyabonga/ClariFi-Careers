import streamlit as st

# --- Custom CSS for branding ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=DM+Sans&display=swap');

    html, body, [class*="css"]  {
        font-family: 'DM Sans', sans-serif;
        color: #0D1B2A;
        background-color: #F9F7F4;
    }

    h1, h2, h3, h4 {
        font-family: 'Playfair Display', serif;
        color: #F4A922;
    }

    /* Button styling */
    .stButton>button {
        background-color: #4CAF82;
        color: #F9F7F4;
        border-radius: 8px;
        font-weight: bold;
    }

    .stButton>button:hover {
        background-color: #0D1B2A;
        color: #F4A922;
    }

    /* Tab styling */
    div[data-baseweb="tab"] {
        font-family: 'Playfair Display', serif;
        font-size: 16px;
        font-weight: 600;
        background-color: #0D1B2A;   /* deep navy */
        color: #F9F7F4;              /* off-white */
        border-radius: 6px 6px 0 0;
        margin-right: 4px;
        padding: 8px 16px;
    }

    div[data-baseweb="tab"]:hover {
        background-color: #4CAF82;   /* muted green */
        color: #F9F7F4;
    }

    div[data-baseweb="tab"][aria-selected="true"] {
        background-color: #F4A922;   /* warm gold */
        color: #0D1B2A;              /* deep navy text */
    }

    /* Privacy note styling */
    .stAlert {
        background-color: #4CAF82 !important;  /* muted green */
        color: #F4A922 !important;             /* warm gold text */
        border-radius: 8px;
        font-weight: bold;
    }

    /* Footer styling */
    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 14px;
        color: #0D1B2A;
    }
    .footer a {
        color: #4CAF82;
        text-decoration: none;
        font-weight: bold;
    }
    .footer a:hover {
        color: #F4A922;
    }
    </style>
""", unsafe_allow_html=True)

# --- Toggle between Testing Mode and Live Mode ---
TESTING_MODE = True   # Change to False when you want to use OpenAI again

# --- Tab Navigation ---
tab1, tab2, tab3, tab4 = st.tabs(["CV Review", "AI Coach", "Learning Hub", "Fun Corner"])

# --- CV REVIEW TAB ---
with tab1:
    st.header("Get Your CV Reviewed")
    st.write("Upload OR paste your CV and get honest, specific feedback — like having a senior hiring manager read your CV over coffee.")

    # Privacy note
    st.info("🔒 Your CV content is used only to generate your review and is not stored on our servers. See our Privacy Policy.")

    uploaded_file = st.file_uploader("Upload CV File", type=["pdf", "docx"])
    cv_text = st.text_area("Paste CV Text")

    if uploaded_file is not None:
        try:
            cv_text = uploaded_file.read().decode("utf-8", errors="ignore")
        except Exception:
            st.error("⚠️ Could not read file. Please paste text instead.")

    if st.button("Review My CV"):
        if cv_text:
            if TESTING_MODE:
                # Dummy recruiter-style feedback (no API call)
                st.markdown(f"""
Thank you for sharing your CV, Candidate.

I'll be very direct, speaking as someone who's reviewed CVs for over 10 years:

- Your CV is visually outdated — heavy borders and shaded boxes make it look pre-2010.
- The layout is not ATS-readable; large sections may be ignored by recruiter systems.
- Font choices, spacing, and alignment are inconsistent and strain the eye.
- The opening headline is weak — it does not position you for a specific role.
- The synopsis is generic, repetitive, and filled with buzzwords without context.
- Core competencies are written as paragraphs instead of sharp, scannable skill statements.

In short: your experience may be strong, but the presentation is actively working against you.
                """)

                # Add "Review another CV" button
                if st.button("↺ Review another CV"):
                    st.experimental_rerun()
            else:
                st.error("⚠️ Live Mode is disabled until billing/API credits are available.")
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

# --- Footer with WhatsApp icon ---
st.markdown("""
<div class="footer">
    Powered by JoyTee Holdings<br>
    © 2025 JoyTee Holdings | ClariFi Career Corner | POPIA Compliant | info@joyteeholdings.co.za<br>
    <a href="https://wa.me/27835290121" target="_blank">💬 Chat with us on WhatsApp</a>
</div>
""", unsafe_allow_html=True)
