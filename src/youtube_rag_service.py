from src.transcript_loader import TranscriptLoader
from src.text_splitter import TextChunker
from src.embedding_model import EmbeddingModel
from src.vector_store import VectorStoreManager
from src.rag_chain import RAGChain

from langchain_groq import ChatGroq

from dotenv import load_dotenv
import os
from youtube_transcript_api import YouTubeTranscriptApi


load_dotenv()


class YouTubeRAGService:

    def __init__(self):

        self.embeddings = EmbeddingModel.load_model()

        self.retriever = None

        self.chat_history = []

        # self.video_duration = 0

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0,
            api_key=os.getenv("GROQ_API_KEY")
        )

    # ==================================================
    # PROCESS VIDEO
    # ==================================================
    def process_video(self, youtube_url):


        transcript = TranscriptLoader.get_transcript(
            youtube_url
        )

        chunks = TextChunker.split_text(
            transcript
        )

        vector_store = VectorStoreManager.create_vector_store(
            chunks,
            self.embeddings
        )

        self.retriever = vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 3,
                "fetch_k": 15,
                "lambda_mult": 0.3
            }
        )

        return len(chunks)

    # ==================================================
    # QUESTION ANSWERING
    # ==================================================
    def ask_question(self, question):

        docs = self.retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        # Last 5 conversations
        previous_chat = "\n".join([
            f"User: {q}\nAssistant: {a}"
            for q, a in self.chat_history[-5:]
        ])

        prompt = f"""
    You are an AI Tutor.

    Use BOTH:

    1. Lecture Context
    2. Previous Conversation

    PREVIOUS CONVERSATION:
    {previous_chat}

    LECTURE CONTEXT:
    {context}

    QUESTION:
    {question}

    Rules:
    - Answer in English
    - Be detailed
    - Use previous conversation if needed
    - If user says:
    'explain more'
    'tell me more'
    'what about that'
    then understand previous discussion

    ANSWER:
    """

        answer = self.llm.invoke(
            prompt
        ).content

        self.chat_history.append(
            (question, answer)
        )

        return {
            "answer": answer,
            "sources": docs
        }

    # ==================================================
    # SUMMARY
    # ==================================================
    def summarize_video(self):

        docs = self.retriever.vectorstore.similarity_search(
            "Complete lecture summary",
            k=10
        )

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        prompt = f"""
You are an expert AI tutor.

Generate output ONLY in English.

Summarize the lecture.

Rules:
- 5 to 10 bullet points
- Simple English
- No Hindi
- No Marathi
- No extra explanation

Lecture:
{context}
"""

        return self.llm.invoke(prompt).content

    # ==================================================
    # MCQ GENERATOR
    # ==================================================
    def generate_mcq(self):

        docs = self.retriever.vectorstore.similarity_search(
            "Important concepts",
            k=10
        )

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        prompt = f"""
You are an expert AI tutor.

Generate output ONLY in English.

Create 5 MCQs.

Rules:
- 4 options each
- Mention correct answer
- Based only on lecture
- No Hindi
- No Marathi

Context:
{context}
"""

        return self.llm.invoke(prompt).content

    # ==================================================
    # KEY POINTS
    # ==================================================
    def key_points(self):

        docs = self.retriever.vectorstore.similarity_search(
            "Main concepts",
            k=10
        )

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        prompt = f"""
You are an expert AI tutor.

Generate output ONLY in English.

Extract key points.

Rules:
- Bullet points only
- Short and clear
- No Hindi
- No Marathi

Context:
{context}
"""

        return self.llm.invoke(prompt).content

    # ==================================================
    # FLASHCARDS
    # ==================================================
    def generate_flashcards(self):

        docs = self.retriever.vectorstore.similarity_search(
            "Important concepts",
            k=10
        )

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        prompt = f"""
You are an expert AI tutor.

Generate output ONLY in English.

Create 10 flashcards.

Format:

Q: Question

A: Answer

Rules:
- Short questions
- Short answers
- Based only on lecture
- No Hindi
- No Marathi

Context:
{context}
"""

        return self.llm.invoke(prompt).content
    
    def generate_mindmap(self):

        docs = self.retriever.vectorstore.similarity_search(
            "Complete lecture structure",
            k=10
        )

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        prompt = f"""
    You are an expert teacher.

    Generate a lecture hierarchy.

    IMPORTANT:
    - English only
    - No explanation
    - Output JSON-like hierarchy

    Format:

    Main Topic
    - Concept 1
        - Subtopic A
        - Subtopic B
    - Concept 2
        - Subtopic C
        - Subtopic D

    Context:
    {context}
    """

        return self.llm.invoke(prompt).content

    def lecture_insights(self):

        docs = self.retriever.vectorstore.similarity_search(
            "overall lecture analysis",
            k=10
        )

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        prompt = f"""
    You are an expert educational analyst.

    IMPORTANT:
    Generate output ONLY in English.

    Analyze the lecture and provide:

    1. Lecture Category
    2. Difficulty Level
    3. Estimated Study Time
    4. Main Topics
    5. Skills Learned

    Rules:
    - Use English only
    - No Hindi
    - No Marathi
    - Professional format
    - Realistic study time based on topic complexity
    - Bullet points

    Context:
    {context}
    """

        return self.llm.invoke(prompt).content