from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Neo4jVector
def connect_and_store_to_neo4j(split):
    try:
        db = Neo4jVector.from_documents(split, OpenAIEmbeddings(), username="neo4j", password="12341234", url="bolt://neo4j:7687")
        return db
    except Exception as e:
        return None