from dotenv import load_dotenv
from src.youtube_rag_service import YouTubeRAGService

load_dotenv()


def main():

    rag = YouTubeRAGService()

    url = input("Enter YouTube URL: ")

    total_chunks = rag.process_video(
        url
    )

    print(
        f"\nVideo Processed Successfully! "
        f"Total Chunks: {total_chunks}"
    )

    while True:

        question = input(
            "\nAsk Question (exit to quit): "
        )

        if question.lower() == "exit":
            break

        result = rag.ask_question(
            question
        )

        print("\nAnswer:\n")
        print(result["answer"])


if __name__ == "__main__":
    main()