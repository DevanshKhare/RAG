from langchain.text_splitter import RecursiveCharacterTextSplitter

def save_content_to_file(content, filename="output.txt"):
    with open(filename, "w", encoding='utf-8') as file:
        file.write("\n".join(content))

def split_text(text, c_size=1000, c_overlap=200):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=c_size, chunk_overlap=c_overlap)
    split=text_splitter.split_documents([text])
    return split
