from src.rag import RAGRetriever
from src.classifier import SupportClassifier
from src.answer_generator import AnswerGenerator


retriever = RAGRetriever(
    "data/knowledge_base.txt"
)

classifier = SupportClassifier(
    retriever,
    threshold=0.30
)

generator = AnswerGenerator()


questions = [
    "How do I reset my password?",
    "I was charged twice",
    "My application is not loading",
    "Can you help me book a flight?"
]


for question in questions:

    print("\n" + "=" * 70)
    print("CUSTOMER:", question)

    result = classifier.classify(question)

    print("STATUS:", result["status"])
    print("CONFIDENCE:", round(result["confidence"], 3))

    if result["status"] == "SUPPORTED":

        answer = generator.generate(
            question,
            result["source"]
        )

        print("\nAI RESPONSE:")
        print(answer)

    else:

        print("\nAI RESPONSE:")
        print(
            "I'm unable to confidently answer this request "
            "using our current knowledge base. "
            "I'm escalating this issue to a human support "
            "representative."
        )