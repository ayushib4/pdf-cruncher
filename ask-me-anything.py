from claude import Claude
import os
from tqdm import tqdm
from PyPDF2 import PdfReader

def ama():
    uploaded = input("Did you upload your document to the documents folder? Y/N ")
    if uploaded == "n" or uploaded == "N": 
        print("Upload the document in the documents folder and try again ")
        ama()
    doc = input("Please type the exact name of the document excluding .pdf ")
    if not os.path.exists("./texts/{doc}.txt"):
        pdf_to_text(doc)
    query_claude(doc)

def pdf_to_text(doc):
    print("Parsing the document and preparing text.")
    reader = PdfReader(f"./documents/{doc}.pdf")
    file = open(f"./texts/{doc}.txt", "a")
    for page in tqdm(reader.pages):
        file.write(page.extract_text())

def query_claude(doc):
    print("Preparing Claude for querying.")
    model = Claude()
    query = input("Ask a question about the document ")
    prompt = "In the following message, you will be provided an academic article. You will then be asked a conceptual question about it, so use the article provided to you to answer that question./n"
    with open(f"./texts/{doc}.txt", 'r', encoding='utf-8') as f:
        prompt = f.read()
    prompt += f"/n{query}"
    res = model(prompt)
    print(res)

if __name__ == "__main__":
    ama()