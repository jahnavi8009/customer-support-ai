from pathlib import Path
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class RAGRetriever:

    def __init__(self, knowledge_base_path):

        self.knowledge_base_path = Path(knowledge_base_path)

        self.documents = self._load_documents()

        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2)
        )

        self.document_vectors = self.vectorizer.fit_transform(
            self.documents
        )

    def _load_documents(self):

        text = self.knowledge_base_path.read_text(
            encoding="utf-8"
        )

        # Split using TITLE markers.
        sections = re.split(
            r"(?=TITLE:)",
            text
        )

        documents = []

        for section in sections:

            section = section.strip()

            if not section:
                continue

            # Ignore sections that don't represent an FAQ/task.
            if not section.startswith("TITLE:"):
                continue

            documents.append(section)

        return documents

    def retrieve(self, query, top_k=3):

        query_vector = self.vectorizer.transform(
            [query]
        )

        similarities = cosine_similarity(
            query_vector,
            self.document_vectors
        )[0]

        ranked_indices = similarities.argsort()[::-1][:top_k]

        results = []

        for index in ranked_indices:

            results.append({
                "text": self.documents[index],
                "score": float(similarities[index])
            })

        return results