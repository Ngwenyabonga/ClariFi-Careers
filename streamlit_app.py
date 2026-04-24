import streamlit as st

# Top tab navigation
tab1, tab2, tab3, tab4 = st.tabs(["CV Review", "AI Coach", "Learning Hub", "Fun Corner"])

with tab1:
    st.write("This is the CV Review page")

with tab2:
    st.write("This is the AI Coach page")

with tab3:
    st.write("This is the Learning Hub page")

with tab4:
    st.write("This is the Fun Corner page")
