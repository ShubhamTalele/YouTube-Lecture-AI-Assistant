from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingModel:

    @staticmethod
    def load_model():

        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )

        return embeddings