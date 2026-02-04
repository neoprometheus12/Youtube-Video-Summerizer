import streamlit as st
from transcript import get_timestamped_transcript
from summarizer import summarize

st.set_page_config(page_title="YouTube Video Summarizer", layout="wide")
st.title("🎥 YouTube Video Summarizer")

url = st.text_input("Enter YouTube video URL")

summary_type = st.selectbox(
    "Select summary type",
    ["Business", "Educational", "Bullet Points", "Snarky"]
)

# Session state to store transcript
if "transcript" not in st.session_state:
    st.session_state.transcript = None

col1, col2 = st.columns(2)

# BUTTON 1: TRANSCRIPT
with col1:
    if st.button("📝 Generate Transcript"):
        if not url:
            st.warning("Please enter a YouTube URL")
        else:
            with st.spinner("Fetching transcript..."):
                st.session_state.transcript = get_timestamped_transcript(url)

# BUTTON 2: SUMMARY
with col2:
    if st.button("✨ Generate Summary"):
        if not st.session_state.transcript:
            st.warning("Please generate transcript first")
        else:
            with st.spinner("Generating summary..."):
                summary = summarize(
                    st.session_state.transcript,
                    summary_type.lower()
                )
                st.session_state.summary = summary

# DISPLAY TRANSCRIPT
if st.session_state.transcript:
    st.subheader("📜 Transcript (Timestamp-wise)")
    st.text_area(
        "Transcript",
        st.session_state.transcript,
        height=300
    )

# DISPLAY SUMMARY
if "summary" in st.session_state:
    st.subheader("📌 Summary")
    st.markdown(st.session_state.summary)

