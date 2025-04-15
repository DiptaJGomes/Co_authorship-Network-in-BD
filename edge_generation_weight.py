import csv
from collections import defaultdict
from itertools import combinations

# Input and output file paths
input_author_uid_csv = "motherfile.csv"  # Input CSV: Author Name, Author ID, UID
input_paper_info_csv = "merged_output.csv"  # Input CSV: Author ID, Paper ID, Title
output_edges_csv = "author_edge_pairs_weighted.csv"  # Output CSV for author UID pairs

# Load author ID to UID mapping
author_id_to_uid = {}
with open(input_author_uid_csv, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        author_id_to_uid[row["Author ID"]] = row["UID"]

# Dictionary to store paper authors
paper_authors = {}

# Read paper information and group authors by paper ID
with open(input_paper_info_csv, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        paper_id = row["Paper ID"].strip()
        author_id = row["Author ID"].strip()
        if author_id in author_id_to_uid:
            if paper_id not in paper_authors:
                paper_authors[paper_id] = []
            paper_authors[paper_id].append(author_id_to_uid[author_id])

# Generate author UID pairs per paper and count occurrences
edge_count = defaultdict(int)
for authors in paper_authors.values():
    if len(authors) > 1:
        for pair in combinations(sorted(authors), 2):
            edge_count[pair] += 1  # Increment the count for this edge

# Write edges and their counts to the output CSV
with open(output_edges_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["UID1", "UID2", "Count"])  # Write header
    for edge, count in edge_count.items():
        writer.writerow([edge[0], edge[1], count])  # Write edge and its count

print(f"Edge pairs between authors have been saved to {output_edges_csv}.")