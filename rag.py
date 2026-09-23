from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class DocumentRetriever:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.documents = []
        self.index = None

    def add_documents(self, documents):

        self.documents.extend(documents)

        embeddings = self.model.encode(
            documents
        )

        embeddings = np.array(
            embeddings,
            dtype="float32"
        )

        self.index = faiss.IndexFlatL2(
            embeddings.shape[1]
        )

        self.index.add(embeddings)

    def search(self, query, top_k=3):

        if not self.documents:
            return []

        query_embedding = self.model.encode(
            [query]
        )

        query_embedding = np.array(
            query_embedding,
            dtype="float32"
        )

        distances, indices = (
            self.index.search(
                query_embedding,
                min(top_k, len(self.documents))
            )
        )

        return [
            self.documents[i]
            for i in indices[0]
        ]
