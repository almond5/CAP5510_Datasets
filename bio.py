import csv
import pandas as pd
from Bio import Entrez
import xml.etree.ElementTree as ET

Entrez.email = "your.email@example.com"

def fetch_abstracts(query, max_records=60):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_records)
    record = Entrez.read(handle)
    ids = record["IdList"]

    abstracts = []
    for id_ in ids:
        handle = Entrez.efetch(db="pubmed", id=id_, rettype="abstract", retmode="xml")
        xml_data = handle.read()
        root = ET.fromstring(xml_data)
        
        for abstract in root.findall(".//Abstract"):
            abstract_text = ""
            for elem in abstract.iter():
                if elem.text:
                    abstract_text += elem.text + " "
            if abstract_text.strip():
                abstracts.append(abstract_text.strip())
        
    return abstracts

query = "What is the best treatment for breast cancer?"
abstracts = fetch_abstracts(query, max_records=60)

# Create a dataframe
df = pd.DataFrame(abstracts, columns=["Abstract"])

# Write the dataframe to a CSV file with UTF-8 encoding
df.to_csv("Question_2.csv", index=False, encoding="utf-8")