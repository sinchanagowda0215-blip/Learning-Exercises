# Simple Document Q&A Application

with open("sample.txt", "r") as file:
    document = file.read()

print("Document loaded successfully.")
print("\nAsk a question about the document.")
print("Type 'exit' to quit.\n")

while True:
    question = input("Question: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    question = question.lower()

    if "office" in question or "located" in question:
        print("Answer: The office is located in Bengaluru.")

    elif "working" in question or "hours" in question:
        print("Answer: Working hours are from 9 AM to 6 PM, Monday to Friday.")

    elif "leave" in question:
        print("Answer: Employees receive 12 days of annual leave every year.")

    elif "insurance" in question:
        print("Answer: The company provides health insurance to employees.")

    else:
        print("Answer: I couldn't find that information in the document.")