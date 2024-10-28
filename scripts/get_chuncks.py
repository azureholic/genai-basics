import os
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import Html2TextTransformer
from langchain_text_splitters import MarkdownHeaderTextSplitter

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

#count files in pages

files = os.listdir("pages")
file_count = len(files)



# for each file in ../pages do
for i in range(0, file_count):
    file_object = open(f"pages/{files[i]}", "r")
    #file nam without extension
    file_name = files[i].split(".")[0]
    
    page = file_object.read()

    # MD splits
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    md_header_splits = markdown_splitter.split_text(page)

    for (i, split) in enumerate(md_header_splits):
        file_object = open(f"chunks/{file_name}-chunk-" + str(i) + ".md", "w")
        file_object.write(split.page_content)
        file_object.close()
