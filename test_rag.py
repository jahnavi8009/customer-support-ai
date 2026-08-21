from src.rag import RAGRetriever


retriever = RAGRetriever(
    "data/knowledge_base.txt"
)


questions = [
    "How do I reset my password?",
    "I was charged twice",
    "My application is not loading",
    "Can you help me book a flight?"
]


for question in questions:

    print("\n" + "=" * 60)
    print("QUESTION:", question)

    results = retriever.retrieve(
        question,
        top_k=2
    )

    for result in results:
        print("\nScore:", round(result["score"], 3))
        print(result["text"][:300])