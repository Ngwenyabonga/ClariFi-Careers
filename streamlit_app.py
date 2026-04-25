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

    /* Tagline styling */
    .tagline {
        position: absolute;
        top: 10px;
        right: 20px;
        font-family: 'Playfair Display', serif;
        font-size: 18px;
        font-weight: bold;
        color: #F4A922;
    }
    </style>
""", unsafe_allow_html=True)

# --- Toggle between Testing Mode and Live Mode ---
TESTING_MODE = True   # Change to False when you want to use OpenAI again

# --- Tagline ---
st.markdown('<div class="tagline">Stop applying. Start positioning.</div>', unsafe_allow_html=True)

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

# --- AI COACH TAB ---
with tab2:
    st.header("AI Coach")
    st.write("This section will provide interactive coaching tips, career positioning strategies, and role-play interview practice.")

    # Dummy coaching prompts for testing
    st.subheader("Practice Prompts")
    st.write("Try answering these common interview questions:")
    st.markdown("""
    - Tell me about yourself.
    - What is your greatest strength?
    - What is your biggest weakness?
    - Why should we hire you?
    - Where do you see yourself in 5 years?
    """)

    if st.button("↺ Reset AI Coach"):
        st.experimental_rerun()

# --- LEARNING HUB TAB ---
with tab3:
    st.header("Learning Hub")
    st.write("Free resources to sharpen your career game — from CV writing to salary negotiation.")

    # Search bar
    search_query = st.text_input("Search resources...", "")

    # Categories
    categories = ["All", "CV Writing", "LinkedIn", "Job Search Strategy", "Interview Prep", "Career Pivots", "Industry Insights"]
    active_category = st.radio("Filter by category:", categories, horizontal=True)

    # Dummy resources with full article text for testing
    resources = [
        {
            "title": "Why Your CV Keeps Getting Ignored (And How to Fix It)",
            "description": "The harsh truth about why most CVs get skipped — and the 5 structural changes that make recruiters stop scrolling.",
            "read_time": "6 min read",
            "category": "CV Writing",
            "content": """
Let's start with a hard truth: most CVs look the same. And in a stack of 200+ applications, "the same" means invisible.

### The Reality of CV Screening
Recruiters in South Africa typically spend 6–10 seconds on an initial CV scan. That's not enough time to read your career history — it's enough time to feel whether your CV is worth reading.

**Here's what gets your CV ignored:**

1. **No Professional Summary (Or a Generic One)**  
   "Dynamic professional seeking challenging opportunities..." — Stop. Every recruiter has read this sentence 10,000 times.  
   Fix: Write a summary that includes your years of experience, your specialisation, one quantifiable achievement, and the value you bring.

2. **Job Descriptions Instead of Achievements**  
   If your CV reads like a job specification, it tells the recruiter what you were supposed to do — not what you actually delivered.  
   Fix: For each role, include 3–5 bullet points that show impact. Use the formula: Action + Context + Result.

3. **Poor Visual Hierarchy**  
   Dense text blocks, inconsistent formatting, tiny fonts, or decorative templates that sacrifice readability.  
   Fix: Use clear section headings, consistent fonts (DM Sans, Calibri, or Arial), plenty of white space, and a logical top-to-bottom flow.

4. **Missing Keywords**  
   Most large companies use Applicant Tracking Systems (ATS). If your CV doesn't contain the right keywords from the job specification, it may never reach human eyes.  
   Fix: Mirror key phrases from the job ad naturally in your CV — especially in your summary, skills, and experience sections.

5. **Too Long or Too Short**  
   A 1-page CV for a senior professional looks light. A 6-page CV for anyone looks unfocused.  
   Fix: The sweet spot for mid-to-senior professionals is 2–3 pages.

### The Bottom Line
Your CV isn't just a document — it's your first negotiation with a potential employer. If it doesn't sell you in 10 seconds, everything else is irrelevant.

**Next step:** Run your CV through a fresh pair of eyes. Not your mom's eyes — a recruiter's eyes.
            """
        },
        # Add other articles here later with same structure
    ]

    # State to track selected article
    if "selected_resource" not in st.session_state:
        st.session_state.selected_resource = None

    # If an article is selected, show full content
    if st.session_state.selected_resource:
        res = st.session_state.selected_resource
        st.subheader(res["title"])
        st.caption(f"📄 {res['category']} • ⏱️ {res['read_time']}")
        st.markdown(res["content"])

        # Monetization banner
        st.markdown("""
        <div style="background-color:#F9F7F4; text-align:center; padding:20px; margin-top:30px; border-radius:8px;">
            <h3 style="color:#0D1B2A;">Ready to put this into action?</h3>
            <p style="color:#0D1B2A;">Book a CV Revamp or LinkedIn session with JoyTee Holdings and get personalised, expert help.</p>
            <a href="https://wa.me/27600000000" target="_blank" style="background-color:#F4A922; color:#0D1B2A; padding:10px 20px; border-radius:6px; text-decoration:none; font-weight:bold;">
                → Book a ClariFi session from R350
            </a>
        </div>
        """, unsafe_allow_html=True)

        if st.button("↺ Back to Learning Hub"):
            st.session_state.selected_resource = None
            st.experimental_rerun()

    else:
        # Filter resources
        filtered_resources = []
        for r in resources:
            matches_category = active_category == "All" or r["category"] == active_category
            matches_search = not search_query or search_query.lower() in r["title"].lower() or search_query.lower() in r["description"].lower()
            if matches_category and matches_search:
                filtered_resources.append(r)

        # Display resource list
        if filtered_resources:
            for res in filtered_resources:
                st.subheader(res["title"])
                st.write(res["description"])
                st.caption(f"⏱️ {res['read_time']}")
                if st.button(f"Read: {res['title']}"):
                    st.session_state.selected_resource = res
                    st.experimental_rerun()
        else:
            st.write("🔍 No resources found. Try a different search or category.")

        if st.button("↺ Reset Learning Hub"):
            st.experimental_rerun()

# --- FUN CORNER TAB ---
with tab4:
    st.header("The Funny Corner 😂")
    st.write("Job searching is stressful. Take a break, have a laugh, and remember — you're not alone in this.")

    # Daily Meme placeholder
    st.subheader("Daily Meme")
    st.write("📸 [Placeholder for Daily Meme image or joke]")

    # Office Bingo placeholder
    st.subheader("Office Bingo")
    st.write("🎲 [Placeholder for interactive Office Bingo game]")

    # Footer note inside Funny Corner
    st.markdown("""
    <div style="text-align:center; margin-top:20px; font-size:12px; color:#0D1B2A;">
        Made with ❤️ and a bit of eish energy. Powered by JoyTee Holdings.
    </div>
    """, unsafe_allow_html=True)

    if st.button("↺ Reset Fun Corner"):
        st.experimental_rerun()
