from Bio import Entrez
Entrez.email = "your.email@example.com"

def fetch_abstracts(query, max_records=100):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_records)
    record = Entrez.read(handle)
    ids = record["IdList"]
    
    abstracts = []
    for id_ in ids:
        handle = Entrez.efetch(db="pubmed", id=id_, rettype="abstract", retmode="text")
        abstract = handle.read()
        abstracts.append(abstract)
    
    return abstracts

query = "antibiotic resistance"
abstracts = fetch_abstracts(query, max_records=1000)
