from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate


class RAGChain:

    @staticmethod
    def answer_question(context, question):

        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0
        )

        prompt = ChatPromptTemplate.from_template("""
        You are an AI Tutor.

        Context:
        {context}

        Question:
        {question}

        Answer in simple English.
        """)

        chain = prompt | llm

        return chain.invoke({
            "context": context,
            "question": question
        }).content

    # ⭐ NEW FEATURE: Lecture Summary
    @staticmethod
    def summarize_lecture(context):

        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0
        )

        prompt = ChatPromptTemplate.from_template("""
        You are an expert educator.

        Summarize the following lecture content into:
        - 10 bullet points
        - Simple English
        - Include all key concepts

        Context:
        {context}

        SUMMARY:
        """)

        chain = prompt | llm

        return chain.invoke({
            "context": context
        }).content
    
    @staticmethod
    def generate_quiz(context):

        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0.3
        )

        prompt = ChatPromptTemplate.from_template("""
        You are an expert teacher.

        Create a quiz from the lecture content.

        Requirements:
        - 5 multiple choice questions
        - 4 options each
        - mark correct answer
        - simple English
        - based ONLY on context

        Context:
        {context}

        QUIZ:
        """)

        chain = prompt | llm

        return chain.invoke({
            "context": context
        }).content