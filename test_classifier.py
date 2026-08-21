from src.rag import RAGRetriever
from src.classifier import SupportClassifier


retriever = RAGRetriever(
    "data/knowledge_base.txt"
)

classifier = SupportClassifier(
    retriever,
    threshold=0.30
)


questions = [
    "How do I reset my password?",
    "I was charged twice",
    "My application is not loading",
    "Can you help me book a flight?"
]


for question in questions:

    result = classifier.classify(question)

    print("\n" + "=" * 60)
    print("QUESTION:", question)
    print("STATUS:", result["status"])
    print("CONFIDENCE:", round(result["confidence"], 3))

    if result["status"] == "SUPPORTED":
        print("SOURCE:")
        print(result["source"][:200])
    else:
        print("ACTION: Escalate to human support")