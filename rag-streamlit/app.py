import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import chromadb

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="RAG Document Chat")

st.title("RAG Document Chat")
st.write("Ask questions about the document.")

# Load document
with open("sample.txt", "r") as file:
    document = file.read()

# Create ChromaDB
chroma_client = chromadb.PersistentClient(path="chroma_db")

collection = chroma_client.get_or_create_collection(
    name="document"
)

# Store document
collection.upsert(
    ids=["document1"],
    documents=[document]
)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
if question := st.chat_input("Ask a question about the document..."):

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    # Retrieve relevant information
    results = collection.query(
        query_texts=[question],
        n_results=1
    )

    context = results["documents"][0][0]

    # Generate answer
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Answer the question using only the provided "
                    "document context. If the answer is not in the "
                    "document, say that the information was not found."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Document context:\n{context}\n\n"
                    f"Question: {question}"
                )
            }
        ]
    )

    answer = response.choices[0].message.content

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.write(answer)

# Clear chat
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()