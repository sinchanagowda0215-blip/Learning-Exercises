import chromadb


# --------------------------------------------------
# 1. Create / open persistent ChromaDB database
# --------------------------------------------------

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="tech_support"
)


# --------------------------------------------------
# 2. Load knowledge-base data
# --------------------------------------------------

with open("data/support_data.txt", "r", encoding="utf-8") as file:
    content = file.read()


# Split the knowledge base into separate documents
documents = [
    section.strip()
    for section in content.split("\n\n")
    if section.strip()
]


# --------------------------------------------------
# 3. Add documents to ChromaDB
# --------------------------------------------------

# Avoid adding duplicate IDs every time the program runs
existing = collection.get()

existing_ids = set(existing["ids"])

new_documents = []
new_ids = []

for i, document in enumerate(documents):
    document_id = f"support_{i}"

    if document_id not in existing_ids:
        new_ids.append(document_id)
        new_documents.append(document)


if new_documents:
    collection.add(
        ids=new_ids,
        documents=new_documents
    )


# --------------------------------------------------
# 4. Display knowledge-base information
# --------------------------------------------------

print("=" * 50)
print("TECH SUPPORT KNOWLEDGE BASE")
print("=" * 50)

print(f"Knowledge-base documents: {collection.count()}")

print("\nAvailable topics:")
print("- Wi-Fi Troubleshooting")
print("- Password Reset")
print("- VPN Troubleshooting")
print("- Software Installation")
print("- Printer Troubleshooting")


# --------------------------------------------------
# 5. Search function
# --------------------------------------------------

def search_knowledge_base(query, number_of_results=2):

    if not query.strip():
        print("\nPlease enter a question.")
        return

    results = collection.query(
        query_texts=[query],
        n_results=number_of_results
    )

    documents_found = results.get("documents", [[]])[0]

    if not documents_found:
        print("\nNo relevant information found.")
        return

    print("\n" + "=" * 50)
    print("SEARCH RESULTS")
    print("=" * 50)

    for index, document in enumerate(documents_found, start=1):

        print(f"\nResult {index}")
        print("-" * 40)
        print(document)


# --------------------------------------------------
# 6. Interactive search
# --------------------------------------------------

while True:

    print("\n")
    query = input(
        "Enter your support question "
        "(or type 'exit' to quit): "
    )

    if query.lower().strip() == "exit":
        print("\nThank you for using the Tech Support Knowledge Base.")
        break

    try:
        search_knowledge_base(query)

    except Exception as error:
        print(f"\nSearch error: {error}")