from langchain_community.vectorstores import FAISS


class VectorStoreManager:

    @staticmethod
    def create_vector_store(
        chunks,
        embeddings
    ):

        return FAISS.from_texts(
            texts=chunks,
            embedding=embeddings
        )

    @staticmethod
    def save_vector_store(
        vector_store,
        path="vector_db"
    ):

        vector_store.save_local(path)

    @staticmethod
    def load_vector_store(
        embeddings,
        path="vector_db"
    ):

        return FAISS.load_local(
            path,
            embeddings,
            allow_dangerous_deserialization=True
        )
    
    @staticmethod
    def load_vector_store(embeddings, path):
        return FAISS.load_local(
            path,
            embeddings,
            allow_dangerous_deserialization=True
        )