# 🎥 YouTube Lecture AI Assistant (RAG)

An AI-powered YouTube Lecture Assistant built using Retrieval-Augmented Generation (RAG), LangChain, FAISS, Groq LLM, and Streamlit.

This application transforms YouTube lectures into an interactive AI Tutor capable of answering questions, generating summaries, creating quizzes, producing flashcards, extracting key concepts, building mind maps, and providing lecture insights.

---

# 🚀 Project Overview

Traditional learning from YouTube videos requires users to repeatedly watch long lectures to understand concepts, revise content, and prepare notes.

This project solves that problem by converting any YouTube lecture into an AI-powered knowledge base that users can interact with through natural language.

Users simply provide a YouTube URL, and the system:

- Extracts lecture transcripts
- Splits content into chunks
- Generates embeddings
- Stores vectors in FAISS
- Retrieves relevant information
- Uses an LLM to generate intelligent responses

---

# 🎯 Problem Statement

Students often face challenges such as:

- Long lecture durations
- Difficulty revising content
- Finding specific topics in videos
- Manually creating notes
- Preparing quizzes and revision material

This system automatically converts lectures into a searchable AI Tutor.

---

# 🏗️ System Architecture

```text
YouTube Video
      │
      ▼
Transcript Extraction
      │
      ▼
Text Chunking
      │
      ▼
Embedding Generation
      │
      ▼
FAISS Vector Database
      │
      ▼
MMR Retriever
      │
      ▼
Groq LLM (Llama 3.3)
      │
      ├── Chat Assistant
      ├── Lecture Summary
      ├── MCQ Generator
      ├── Flashcards
      ├── Key Points
      ├── Mind Map
      └── Lecture Insights
```

---

# 🔄 Complete Project Workflow

## Step 1: User Inputs YouTube URL

Example:

```text
https://www.youtube.com/watch?v=xxxxxxxx
```

---

## Step 2: Transcript Extraction

Library Used:

```python
youtube-transcript-api
```

Purpose:

- Fetch lecture captions
- Convert video content into text

Output:

```text
Raw Lecture Transcript
```

---

## Step 3: Text Chunking

Component:

```python
RecursiveCharacterTextSplitter
```

Purpose:

- Break large transcripts into smaller chunks
- Improve retrieval quality
- Avoid LLM context overload

Output:

```text
Chunk 1
Chunk 2
Chunk 3
...
```

---

## Step 4: Embedding Generation

Embedding Model:

```python
sentence-transformers/all-MiniLM-L6-v2
```

Purpose:

- Convert text into vectors
- Capture semantic meaning

Example:

```text
"What is RAG?"
        ↓
[0.12, 0.45, 0.67, ...]
```

---

## Step 5: Vector Database Storage

Vector Database:

```python
FAISS
```

Purpose:

- Store embeddings
- Enable semantic search
- Fast retrieval

---

## Step 6: Retrieval

Retriever Type:

```python
MMR (Maximal Marginal Relevance)
```

Configuration:

```python
search_type="mmr"

search_kwargs={
    "k": 3,
    "fetch_k": 15,
    "lambda_mult": 0.3
}
```

Benefits:

- Retrieves relevant chunks
- Reduces duplicate context
- Improves answer quality

---

## Step 7: LLM Generation

Model:

```python
llama-3.3-70b-versatile
```

Provider:

```python
Groq
```

Purpose:

- Answer questions
- Generate summaries
- Create flashcards
- Generate MCQs
- Produce insights

---

# 🧠 Features Implemented

## 1️⃣ AI Chat Assistant

Ask questions about the lecture.

Example:

```text
What is LangGraph?
```

The system:

- Retrieves relevant chunks
- Sends context to LLM
- Generates answer

---

## 2️⃣ Lecture Summary

Generates:

- Main concepts
- Important ideas
- Lecture overview

Output:

```text
5-10 bullet points
```

---

## 3️⃣ MCQ Generator

Generates:

- 5 Multiple Choice Questions
- 4 options per question
- Correct answer included

Useful for:

- Revision
- Self-assessment
- Interview preparation

---

## 4️⃣ Flashcards

Generates:

```text
Q: What is RAG?

A: Retrieval Augmented Generation
```

Useful for:

- Quick revision
- Memorization

---

## 5️⃣ Key Points Extraction

Extracts:

- Important concepts
- Core ideas
- Main topics

Output:

```text
• Concept 1
• Concept 2
• Concept 3
```

---

## 6️⃣ Lecture Mind Map

Creates hierarchical lecture structure.

Example:

```text
Machine Learning
├── Supervised Learning
│   ├── Regression
│   └── Classification
├── Unsupervised Learning
│   ├── Clustering
│   └── Association
```

Useful for:

- Visual understanding
- Topic relationships

---

## 7️⃣ Lecture Insights

Generates:

### Lecture Category

Example:

```text
Artificial Intelligence
```

### Difficulty Level

Example:

```text
Beginner
Intermediate
Advanced
```

### Main Topics

Example:

```text
RAG
Embeddings
FAISS
```

### Skills Learned

Example:

```text
Prompt Engineering
Vector Search
LangChain
```

---

## 8️⃣ Conversational Memory

Implemented Memory:

```python
self.chat_history
```

Purpose:

- Remembers recent conversations
- Understands follow-up questions

Example:

```text
User: Explain RAG

User: Explain more
```

The assistant understands the previous context.

---

# 🛠️ Tech Stack

## Frontend

### Streamlit

Purpose:

- Interactive UI
- Chat interface
- Dashboard

---

## Backend

### Python

Purpose:

- Business logic
- Data processing
- RAG implementation

---

## Framework

### LangChain

Purpose:

- RAG pipeline
- Prompt management
- Retriever integration

Components Used:

```python
ChatPromptTemplate
Runnable Chains
Retriever
```

---

## LLM

### Groq

Model:

```python
llama-3.3-70b-versatile
```

Purpose:

- Natural language generation
- Summaries
- Quiz creation

---

## Vector Database

### FAISS

Purpose:

- Store embeddings
- Similarity search

---

## Embedding Model

### Sentence Transformers

Model:

```python
all-MiniLM-L6-v2
```

Purpose:

- Text vectorization

---

## Transcript Extraction

### youtube-transcript-api

Purpose:

- Extract YouTube captions

---

# 📂 Project Structure

```text
youtube-rag/
│
├── streamlit_app.py
│
├── requirements.txt
│
├── README.md
│
├── .env
│
├── src/
│   │
│   ├── youtube_rag_service.py
│   ├── transcript_loader.py
│   ├── text_splitter.py
│   ├── embedding_model.py
│   ├── vector_store.py
│   ├── rag_chain.py
│   └── retriever.py
│
└── memory/
```

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/youtube-rag.git

cd youtube-rag
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment:

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create:

```text
.env
```

Add:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## Run Application

```bash
streamlit run streamlit_app.py
```

---

# 📊 Sample Use Cases

### Student Revision

Upload lecture

Generate:

- Summary
- Flashcards
- MCQs

---

### Interview Preparation

Upload technical lecture

Ask:

```text
Explain FAISS

Explain Embeddings

Difference between RAG and Fine Tuning
```

---

### Course Learning

Upload educational content

Generate:

- Mind maps
- Key points
- Notes

---

# 🔮 Future Enhancements

Planned Improvements:

- Persistent Memory (JSON)
- FAISS Chat Memory
- Multi-Video Knowledge Base
- PDF Notes Export
- Visual Graph Mind Maps
- User Authentication
- Agentic AI Tutor
- Multi-Language Support
- Lecture Comparison

---

# 🎓 Concepts Demonstrated

This project demonstrates:

- Retrieval Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- Embeddings
- Prompt Engineering
- Conversational AI
- Information Retrieval
- Streamlit Development
- LLM Integration
- LangChain Framework

---

# 💡 Interview Questions This Project Can Answer

### What is RAG?

Retrieval-Augmented Generation combines information retrieval with Large Language Models to provide context-aware answers.

---

### Why FAISS?

FAISS enables efficient similarity search over vector embeddings.

---

### Why Embeddings?

Embeddings convert text into numerical vectors that preserve semantic meaning.

---

### Why MMR Retriever?

MMR reduces duplicate retrieval and improves context diversity.

---

### Why LangChain?

LangChain simplifies the development of LLM-powered applications and RAG pipelines.

---

### Difference Between Traditional Search and Semantic Search?

Traditional Search:
- Keyword matching

Semantic Search:
- Meaning-based retrieval using embeddings

---

# 👨‍💻 Author

Shubham Talele

PG-Diploma in Data Science & Big Data Analytics (CDAC Mumbai)

Skills:

- Python
- SQL
- PySpark
- Azure
- AWS
- LangChain
- Generative AI
- RAG
- Machine Learning
- Data Engineering

---

# ⭐ If you found this project useful, consider giving it a star.