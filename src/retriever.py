from src.vector_store import VectorStoreManager


class RetrieverManager:

    @staticmethod
    def get_retriever(embeddings, vector_store_path):

        # Load FAISS index
        vector_store = VectorStoreManager.load_vector_store(
            embeddings,
            vector_store_path
        )

        # 🔥 Better retrieval configuration
        retriever = vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 3,
                "fetch_k": 15,
                "lambda_mult": 0.3
            }
        )

        return retriever