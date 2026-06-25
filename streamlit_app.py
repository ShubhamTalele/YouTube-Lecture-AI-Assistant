import streamlit as st
from src.youtube_rag_service import YouTubeRAGService

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="YouTube AI Tutor",
    page_icon="🎥",
    layout="wide"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.stButton button {
    width:100%;
    border-radius:10px;
}

.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# SESSION STATE
# ==================================================

if "rag" not in st.session_state:
    st.session_state.rag = YouTubeRAGService()

if "video_ready" not in st.session_state:
    st.session_state.video_ready = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chunks" not in st.session_state:
    st.session_state.chunks = 0

# ==================================================
# HEADER
# ==================================================

st.title("🎥 YouTube Lecture AI Assistant")

st.markdown("""
Turn any YouTube lecture into:

✅ AI Chat Tutor

✅ Lecture Summary

✅ MCQ Quiz

✅ Flashcards

✅ Key Concepts

✅ Lecture Mind Map

Powered by LangChain + FAISS + Groq + Streamlit
""")

st.divider()

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("⚙ Features")

page = st.sidebar.radio(
    "Select",
    [
        "Process Video",
        "Chat Assistant",
        "Summary",
        "MCQ Quiz",
        "Flashcards",
        "Key Points",
        "Mind Map",
        "Lecture Insights"
    ]
)

# ==================================================
# PROCESS VIDEO
# ==================================================

if page == "Process Video":

    st.header("📥 Load YouTube Lecture")

    url = st.text_input(
        "Paste YouTube URL"
    )

    if st.button("Process Video"):

        if url:

            with st.spinner("Processing Lecture..."):

                chunks = (
                    st.session_state.rag
                    .process_video(url)
                )

            st.session_state.video_ready = True
            st.session_state.chunks = chunks

            st.success(
                "Video Processed Successfully!"
            )

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Chunks",
                chunks
            )

            c2.metric(
                "Retriever",
                "MMR"
            )

            c3.metric(
                "Model",
                "Llama 3.3"
            )

# ==================================================
# CHECK VIDEO
# ==================================================

elif not st.session_state.video_ready:

    st.warning(
        "Please process a YouTube video first."
    )

# ==================================================
# CHAT ASSISTANT
# ==================================================

elif page == "Chat Assistant":

    st.header("💬 AI Tutor")

    question = st.chat_input(
        "Ask anything about the lecture..."
    )

    if question:

        with st.chat_message("user"):
            st.write(question)

        result = (
            st.session_state.rag
            .ask_question(question)
        )

        answer = result["answer"]

        with st.chat_message("assistant"):
            st.write(answer)

        st.session_state.chat_history.append(
            (question, answer)
        )

        st.subheader("📚 Retrieved Sources")

        for doc in result["sources"]:

            with st.expander("Source Chunk"):

                st.write(
                    doc.page_content
                )

# ==================================================
# SUMMARY
# ==================================================

elif page == "Summary":

    st.header("🧾 Lecture Summary")

    if st.button("Generate Summary"):

        with st.spinner("Generating..."):

            summary = (
                st.session_state.rag
                .summarize_video()
            )

        st.success("Done")

        st.markdown(summary)

# ==================================================
# MCQ
# ==================================================

elif page == "MCQ Quiz":

    st.header("🧠 Lecture Quiz")

    if st.button("Generate MCQs"):

        with st.spinner("Generating Quiz..."):

            mcq = (
                st.session_state.rag
                .generate_mcq()
            )

        st.success("Done")

        st.markdown(mcq)

# ==================================================
# FLASHCARDS
# ==================================================

elif page == "Flashcards":

    st.header("🗂 Flashcards")

    if st.button("Generate Flashcards"):

        with st.spinner("Creating Flashcards..."):

            flashcards = (
                st.session_state.rag
                .generate_flashcards()
            )

        st.success("Done")

        st.markdown(flashcards)

# ==================================================
# KEY POINTS
# ==================================================

elif page == "Key Points":

    st.header("📌 Key Concepts")

    if st.button("Generate Key Points"):

        with st.spinner("Extracting Concepts..."):

            points = (
                st.session_state.rag
                .key_points()
            )

        st.success("Done")

        st.markdown(points)

# ==================================================
# MIND MAP
# ==================================================

elif page == "Mind Map":

    st.header("🧠 Lecture Mind Map")

    if st.button("Generate Mind Map"):

        with st.spinner("Creating Mind Map..."):

            mindmap = (
                st.session_state.rag
                .generate_mindmap()
            )

        st.success("Done")

        st.text(mindmap)

elif page == "Lecture Insights":

    st.header("📊 Lecture Insights")

    if st.button("Generate Insights"):

        with st.spinner("Analyzing Lecture..."):

            insights = (
                st.session_state.rag
                .lecture_insights()
            )

        st.success("Done")

        st.markdown(insights)

# ==================================================
# CHAT HISTORY
# ==================================================

if st.session_state.chat_history:

    st.divider()

    st.subheader("🕒 Previous Questions")

    for q, a in reversed(
        st.session_state.chat_history
    ):

        with st.expander(q):

            st.write(a)
st.sidebar.metric("Chunks", st.session_state.chunks)
st.sidebar.metric("Model", "Llama 3.3")
st.sidebar.metric("Retriever", "MMR")

if st.sidebar.button("Clear Chat"):
    st.session_state.chat_history = []
    st.session_state.rag.chat_history = []

st.download_button(
    "Download Summary",
    summary,
    file_name="lecture_summary.txt"
)

st.download_button(
    "Download Flashcards",
    flashcards,
    file_name="flashcards.txt"
)

st.download_button(
    "Download Summary",
    summary,
    file_name="summary.txt"
)

st.sidebar.markdown("## Project Info")

st.sidebar.info("""
Model: Llama 3.3 70B

Embeddings:
all-MiniLM-L6-v2

Vector Store:
FAISS

Retriever:
MMR

Framework:
LangChain
""")

if st.sidebar.button("Clear Chat"):
    st.session_state.chat_history = []
    st.session_state.rag.chat_history = []
    st.success("Chat Cleared")

st.metric("Chunks", chunks)
st.metric("Retriever", "MMR")
st.metric("Embedding Model", "MiniLM")

