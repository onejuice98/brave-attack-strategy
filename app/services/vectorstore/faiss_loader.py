import os
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.config.settings import settings


def build_faiss_vectorstore(
    knowledge_base_dir: str = "data/knowledge_base",
    save_path: str = "data/vector_store",
):
    # 1. 문서 불러오기 (모든 하위 폴더 포함)
    documents = []
    for root, _, files in os.walk(knowledge_base_dir):
        for filename in files:
            if filename.endswith(".txt"):
                filepath = os.path.join(root, filename)
                loader = TextLoader(filepath)
                documents.extend(loader.load())

    if not documents:
        raise ValueError(
            f"[ERROR] No .txt documents found in {knowledge_base_dir} or subfolders."
        )

    # 2. 문서 분할
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=100, separators=["\n\n", "\n", ".", " "]
    )
    split_docs = splitter.split_documents(documents)

    # 3. 임베딩 모델 준비
    embedding = OpenAIEmbeddings(openai_api_key=settings.openai_api_key)

    # 4. FAISS 인덱싱
    vectorstore = FAISS.from_documents(split_docs, embedding)

    # 5. 저장
    vectorstore.save_local(save_path)
    print(f"[FAISS] 저장 완료: {save_path}")


if __name__ == "__main__":
    build_faiss_vectorstore()
