import pandas as pd
import re

def clean_abstracts(file_path, output_path):
    df = pd.read_csv(file_path)

    # Define a function to remove author information
    def remove_author_info(text):
        # Regular expression patterns to match author information
        patterns = [
            r'Author information:.*',  # Matches lines starting with 'Author information:'
            r'\(\d+\).*',  # Matches lines with author details in parentheses (e.g., (1)Department...)
            r'Conflict of interest statement:.*',  # Matches lines starting with 'Conflict of interest statement:'
            r'Copyright.*',  # Matches lines starting with 'Copyright'
            r'DOI:.*',  # Matches lines starting with 'DOI:'
            r'PMID:.*',  # Matches lines starting with 'PMID:'
            r'PMCID:.*',  # Matches lines starting with 'PMCID:'
            r'Erratum in.*',  # Matches lines starting with 'Erratum in'
            r'Comment on.*',  # Matches lines starting with 'Comment on'
            r'©.*',  # Matches lines starting with '©'
        ]
        for pattern in patterns:
            text = re.sub(pattern, '', text)
        return text.strip()

    df['Abstract'] = df['Abstract'].apply(remove_author_info)

    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_file = 'Question_1.csv'
    output_file = 'cleaned_abstracts.csv'

    # Clean the abstracts
    clean_abstracts(input_file, output_file)