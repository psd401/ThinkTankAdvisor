import os
from typing import List

from langchain_pinecone import Pinecone, PineconeClient
from langchain.schema import Document
from langchain_community.vectorstores import Pinecone
from langchain_community.embeddings import OpenAIEmbeddings

class PineconeDB:
    def __init__(self, index_name: str, embedding_source: str):
        self.index_name = index_name
        self.initialise_pinecone()
        self.vector_store = Pinecone(
            index=self.get_index(),
            embedding=get_embeddings_from_source(embedding_source),
            text_key="text",
        )

    def save_documents_as_embeddings(self, docs: List[Document]):
        self.vector_store.add_documents(documents=docs)

    def initialise_pinecone(self):
        api_key = os.environ.get("PINECONE_API_KEY")
        self.pc_client = PineconeClient(api_key=api_key)
        if self.index_name not in self.pc_client.list_indexes():
            self.pc_client.create_index(
                name=self.index_name,
                dimension=1536,
                metric='euclidean',
                spec=ServerlessSpec(
                    cloud='aws',
                    region='us-west-2'
                )
            )

    def get_index(self, num_pool_threads: int = 4):
        return pinecone.Index(self.index_name, pool_threads=num_pool_threads)

    def get_similar_docs(self, query: str, top_k: int = 3):
        similar_docs = self.vector_store.similarity_search(query=query, k=top_k)

        return similar_docs


def get_embeddings_from_source(source: str):
    embedding_source_map = {"open-ai": OpenAIEmbeddings()}

    return embedding_source_map[source]
