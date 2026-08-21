class SupportClassifier:

    def __init__(self, retriever, threshold=0.30):

        self.retriever = retriever
        self.threshold = threshold

    def classify(self, query):

        results = self.retriever.retrieve(
            query,
            top_k=1
        )

        best_result = results[0]

        score = best_result["score"]

        if score >= self.threshold:

            return {
                "status": "SUPPORTED",
                "confidence": score,
                "source": best_result["text"]
            }

        else:

            return {
                "status": "ESCALATE",
                "confidence": score,
                "source": None
            }