# Document Q&A RAG

A simple Document Question & Answer application built using Retrieval-Augmented Generation (RAG).

## How It Works

The application:

1. Loads information from a text document.
2. Stores the document in ChromaDB.
3. Retrieves relevant information based on the user's question.
4. Sends the retrieved context to the OpenAI model.
5. Generates an answer based only on the document.

## Project Structure

```text
document-qa/
├── main.py
├── sample.txt
├── requirements.txt
└── README.md