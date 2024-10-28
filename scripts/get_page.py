from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import Html2TextTransformer


pagesToLoad = [
    "https://www.sintjan-lvo.nl/",
    "https://www.sintjan-lvo.nl/nieuws/2024/10/informatieavond-5-november/"
    
]


loader = AsyncChromiumLoader(pagesToLoad)
html = loader.load()

html2text = Html2TextTransformer()
docs_transformed = html2text.transform_documents(html)

for (i, doc) in enumerate(docs_transformed):
    if i == 0:
        pageName = "home"
    else:
        pageName = pagesToLoad[i].split("/")[-2]

    with open(f"pages/{pageName}.md", "w", encoding="utf-8") as file_object:
        file_object.write(doc.page_content)

