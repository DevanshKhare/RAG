from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
llm = ChatOpenAI()

def generate_response(retriever, input):
    prompt = ChatPromptTemplate.from_template("""Answer the following questions based on the provided context.
    <context>
    {context}
    </context>
    Question: {input}
    """)

    document_chain=create_stuff_documents_chain(llm, prompt)
    retrieval_chain=create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({"input": input})
    return response["answer"]
