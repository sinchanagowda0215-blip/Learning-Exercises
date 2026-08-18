# ChromaDB Tech Support Knowledge Base

## 1. Project Overview

This project demonstrates how to build a searchable knowledge base using ChromaDB.

The knowledge base contains common technical support information such as:

- Wi-Fi troubleshooting
- Password reset
- VPN troubleshooting
- Software installation
- Printer troubleshooting

Users can enter a natural-language question, and ChromaDB retrieves the most relevant support information.

---

## 2. Project Architecture

The application follows this flow:

User Question
↓
ChromaDB Semantic Search
↓
Relevant Knowledge Base Documents
↓
Display Search Results

---

## 3. Project Structure

```text
chromadb-knowledge-base/
│
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│   └── support_data.txt
│
└── chroma_db/
    └── Persistent ChromaDB storage