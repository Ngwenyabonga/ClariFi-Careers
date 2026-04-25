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

    # Dummy resources for testing
    resources = [
        {"title": "Why Your CV Keeps Getting Ignored (And How to Fix It)",
         "description": "The harsh truth about why most CVs get skipped — and the 5 structural changes that make recruiters stop scrolling.",
         "read_time": "6 min read",
         "category": "CV Writing"},
        {"title": "The LinkedIn Profile Sections Most Professionals Neglect",
         "description": "Your LinkedIn headline, About section, and Featured area are prime real estate. Here’s how to use them.",
         "read_time": "7 min read",
         "category": "LinkedIn"},
        {"title": "How Recruiters Actually Screen CVs in Under 10 Seconds",
         "description": "A peek behind the curtain at exactly what recruiters look at first — and what they skip entirely.",
         "read_time": "5 min read",
         "category": "Job Search Strategy"},
        {"title": "Salary Negotiation: What to Say When They Ask ‘What Are You Expecting?’",
         "description": "The dreaded salary question doesn’t have to be a trap. Here’s how to answer with confidence.",
         "read_time": "8 min read",
         "category": "Salary Negotiation"},
        {"title": "Interview Preparation Framework: The STAR Method Explained",
         "description": "The most effective way to answer competency-based interview questions — with South African examples.",
         "read_time": "7 min read",
         "category": "Interview Prep"},
        {"title": "How to Pivot Industries Without Starting From Zero",
         "description": "Changing careers doesn’t mean losing your experience. Here’s how to reframe your skills for a new industry.",
         "read_time": "7 min read",
         "category": "Career Pivots"},
        {"title": "The Hidden Job Market: 70% of Jobs Are Never Advertised",
         "description": "Most job openings are filled before they hit job boards. Here’s how to access the ones you never see.",
         "read_time": "6 min read",
         "category": "Industry Insights"},
    ]

    # Filter logic
    filtered_resources = []
    for r in resources:
        matches_category = active_category == "All" or r["category"] == active_category
        matches_search = not search_query or search_query.lower() in r["title"].lower() or search_query.lower() in r["description"].lower()
        if matches_category and matches_search:
            filtered_resources.append(r)

    # Display resources
    if filtered_resources:
        for res in filtered_resources:
            st.subheader(res["title"])
            st.write(res["description"])
            st.caption(f"⏱️ {res['read_time']}")
            if st.button(f"Read: {res['title']}"):
                st.info(f"[Placeholder] Viewing resource: {res['title']}")
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
