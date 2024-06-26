import requests
from bs4 import BeautifulSoup, SoupStrainer
from langchain_community.document_loaders import WebBaseLoader

def extract_content(website, target_words=["ai", "hr"]):

    extracted_content = []

    try:
        response = requests.get(website)
        response.raise_for_status()

        main_section = SoupStrainer(class_=lambda class_: class_ in ("wd_title", "hello"))
        soup = BeautifulSoup(response.content, 'html.parser', parse_only=main_section)


        links = soup.find_all("a", href=True)
        all_links = []

        for link in links:
            href=link.get('href')
            all_links.append(href)


        if(all_links.__len__()>0):
            for link in all_links:
                response = requests.get(link)
                response.raise_for_status()

                soup = BeautifulSoup(response.content,"html.parser")
                body=soup.find("body").get_text()
                strippedbody=" ".join(body.split())
                extracted_content.append(strippedbody)


    except requests.exceptions.RequestException as e:
        print(f"Error encountered while fetching content: {e}")


    return extracted_content
