from langchain.vectorstores import FAISS
from langchain.embeddings import GPT4AllEmbeddings

class Memory:
    def __init__(self, **kwargs):
        self._embeddings = GPT4AllEmbeddings()

    def get_embeddings(self):
        return self._embeddings

