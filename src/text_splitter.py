from langchain.text_splitter import RecursiveCharacterTextSplitter


class TextChunker:

    @staticmethod
    def split_text(text):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=400,
            chunk_overlap=80
        )

        return splitter.split_text(text)