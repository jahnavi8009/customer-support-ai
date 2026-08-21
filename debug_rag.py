from src.rag import RAGRetriever

retriever = RAGRetriever(
    "data/knowledge_base.txt"
)

print("\nTOTAL DOCUMENTS:", len(retriever.documents))

for i, document in enumerate(retriever.documents):
    print("\n" + "=" * 70)
    print("DOCUMENT", i + 1)
    print(document[:500])