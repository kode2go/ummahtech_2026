# app.py
import streamlit as st

st.set_page_config(
    page_title="Tech Sovereignty: Building What We Control",
    page_icon="☁️",
    layout="centered"
)

st.title("Ummah Tech 2026")
st.subheader("Tech Sovereignty: Building What We Control")

st.markdown(
    """
Thank you for attending the talk.

This page brings together the key links mentioned during the session.

### Contact

📧 **Email:** [bbarsch@gmail.com](mailto:bbarsch@gmail.com)  
🔗 **LinkedIn:** [Binyamin Barsch](https://www.linkedin.com/in/binjamin-binyamin-barsch-43036216a/)
"""
)

st.divider()

st.header("Talk Slides")
st.markdown(
    """
Download or view the slides:
"""
)

st.link_button(
    "📄 Download Talk Slides (PDF)",
    "https://raw.githubusercontent.com/kode2go/pyconza_2026/main/Python, AI Agents, and the Future of Infrastructure Automation_v2.pdf"
    
)


st.divider()
st.header("Offline AI")
st.markdown(
    """
Offline local AI for your laptop or phone!
"""
)
st.link_button("Link", "https://kode2go.github.io/ai_offline/")
st.divider()

st.header("CHPC - Centre for High Performance Computing")
st.markdown(
    """
To know more about CHPC and local compute and cloud resources:
"""
)
st.link_button("Visit CHPC", "https://chpc.ac.za")

st.caption("CHPC | Local compute, cloud access, and responsible AI")
