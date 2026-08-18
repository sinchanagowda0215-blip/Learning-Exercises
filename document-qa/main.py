import os
from dotenv import load_dotenv
from openai import OpenAI
import chromadb

# Load API key
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load document
with open("sample.txt", "r") as file:
    document = file.read()

# Create ChromaDB database
chroma_client = chromadb.PersistentClient(path="chroma_db")

collection = chroma_client.get_or_create_collection(
    name="documents"
)

# Store document
collection.upsert(
    ids=["document1"],
    documents=[document]
)

print("Document loaded successfully.")
print("RAG system is ready.")
print("Ask questions about the document.")
print("Type 'exit' to quit.\n")

while True:
    question = input("Question: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Retrieve relevant document content
    results = collection.query(
        query_texts=[question],
        n_results=1
    )

    context = results["documents"][0][0]

    # Ask the LLM using retrieved context
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Answer the user's question using only the provided "
                    "document context. If the answer is not in the context, "
                    "say that the information was not found in the document."
                )
            },
            {
                "role": "user",
                "content": f"Document context:\n{context}\n\nQuestion: {question}"
            }
        ]
    )

    answer = response.choices[0].message.content

    print(f"\nAnswer: {answer}\n")