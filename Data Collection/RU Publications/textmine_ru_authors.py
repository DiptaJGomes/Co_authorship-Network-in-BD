import csv
import re

# Input data
research_data = """
"""

# Pattern to extract authors and titles
def extract_authors_and_titles(data):
    pattern = r"(?:\d+\.\s)(.+?)\"(.+?)\""
    matches = re.findall(pattern, data)
    return matches

# Extracted data
extracted_data = extract_authors_and_titles(research_data)

# Write to CSV
csv_file = "research_authors_titles.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Authors", "Title"])
    for authors, title in extracted_data:
        writer.writerow([authors.strip(), title.strip()])

print(f"Data successfully written to {csv_file}.")