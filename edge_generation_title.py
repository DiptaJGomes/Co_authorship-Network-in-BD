import csv
from itertools import combinations
from collections import defaultdict

# Input and output file paths
input_author_uid_csv = "motherfile.csv"  # Input CSV: Author Name, Author ID, UID
input_paper_info_csv = "merged_output.csv"  # Input CSV: Author ID, Paper ID, Title
output_edges_csv = "author_edge_pairs_with_titles.csv"  # Output CSV for author UID pairs with titles

# Load author ID to UID mapping
author_id_to_uid = {}
with open(input_author_uid_csv, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        author_id_to_uid[row["Author ID"]] = row["UID"]

# Dictionary to store paper authors and titles
paper_authors = {}
paper_titles = {}

# Read paper information and group authors by paper ID
with open(input_paper_info_csv, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        paper_id = row["Paper ID"].strip()
        author_id = row["Author ID"].strip()
        title = row["Title"].strip()  # Extract the paper title

        # Store the title for the paper
        if paper_id not in paper_titles:
            paper_titles[paper_id] = title

        # Map authors to their respective paper IDs
        if author_id in author_id_to_uid:
            if paper_id not in paper_authors:
                paper_authors[paper_id] = []
            paper_authors[paper_id].append(author_id_to_uid[author_id])

# Generate author UID pairs per paper and map titles
edges_with_titles = []
for paper_id, authors in paper_authors.items():
    if len(authors) > 1:
        title = paper_titles[paper_id]  # Get the title for the current paper
        for pair in combinations(sorted(authors), 2):
            edges_with_titles.append((pair[0], pair[1], title))  # Include title in the edge

# Write edges and titles to the output CSV
with open(output_edges_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["UID1", "UID2", "Title"])  # Write header
    writer.writerows(edges_with_titles)

print(f"Edge pairs between authors along with titles have been saved to {output_edges_csv}.")