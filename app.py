import os
import streamlit as st
from transcript import get_timestamped_transcript
from summarizer import summarize

# Detect Streamlit Cloud
IS_CLOUD = os.getenv("STREAMLIT_SERVER_HEADLESS") == "true"

st.set_page_config(page_title="YouTube Video Summarizer", layout="wide")
st.title("🎥 YouTube Video Summarizer")

url = st.text_input("Enter YouTube Video URL")

summary_type = st.selectbox(
    "Select Summary Type",
    ["Overview", "Educational", "Bullet Points", "Insights", "Snarky"]
)

if "transcript" not in st.session_state:
    st.session_state.transcript = None

if "summary" not in st.session_state:
    st.session_state.summary = None

col1, col2 = st.columns(2)

with col1:
    if st.button("📝 Generate Transcript"):
        if not url:
            st.warning("Please enter a YouTube URL")
        else:
            with st.spinner("Fetching transcript..."):
                transcript = get_timestamped_transcript(url)

                if not transcript:
                    st.error(
                        "❌ This video does not provide captions.\n\n"
                        "Audio transcription is disabled on cloud deployments "
                        "due to YouTube restrictions."
                    )
                    st.stop()

                st.session_state.transcript = transcript
                st.session_state.summary = None

with col2:
    if st.button("✨ Generate Summary"):
        if not st.session_state.transcript:
            st.warning("Generate transcript first")
        else:
            with st.spinner("Generating summary..."):
                st.session_state.summary = summarize(
                    st.session_state.transcript,
                    summary_type.lower()
                )

if st.session_state.transcript:
    st.subheader("📜 Timestamp-wise Transcript")
    st.text_area("Transcript", st.session_state.transcript, height=300)

if st.session_state.summary:
    st.subheader("📌 Summary")
    st.markdown(st.session_state.summary)
