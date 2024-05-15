
from dotenv import load_dotenv
from lib.webscraper import extract_content
from lib.helpers import save_content_to_file, split_text
from langchain.docstore.document import Document
from lib.neo4j import connect_and_store_to_neo4j
from lib.chains import generate_response
import streamlit as st

load_dotenv()

try:
    st.title("AI Sensing")
    input_text = st.text_input("Search the topic you want")


    extracted_content = extract_content("https://newsroom.workday.com/press-releases")

    joined = " ".join(extracted_content)
    save_content_to_file(extracted_content)

    content_document = Document(page_content=joined, metatdata={"source": "https://newsroom.workday.com/press-releases"})
            

    split = split_text(content_document, 1000, 200)

    db = connect_and_store_to_neo4j(split)
    retriever=db.as_retriever()

    if input_text:
        response = generate_response(retriever, input_text)
        st.write(response)
except Exception as e:
    st.error(f"An error occurred: {str(e)}")





