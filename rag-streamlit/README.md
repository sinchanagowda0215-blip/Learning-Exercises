# RAG Streamlit Application

A simple Retrieval-Augmented Generation (RAG) application with a Streamlit chat interface.

## Features

- Streamlit chat interface
- Document-based question answering
- ChromaDB for document retrieval
- OpenAI for answer generation
- Conversation history
- Clear chat option

## How It Works

```text
Document
   ↓
ChromaDB
   ↓
Retrieve relevant context
   ↓
OpenAI
   ↓
Generate answer
   ↓
Streamlit chat interface