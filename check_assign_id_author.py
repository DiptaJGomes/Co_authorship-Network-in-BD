import csv
import re

# Input file paths
uid_author_csv = "path/to/uid_author.csv"  # First CSV: UID and Author Name
name_id_csv = "path/to/name_id.csv"  # Second CSV: Author Name and Author ID
output_csv = "merged_authors.csv"  # Output CSV

# Load UID and author names from the first CSV
uid_author_map = {}
with open(uid_author_csv, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader, None)  # Skip header
    for row in reader:
        if row:
            uid, author_name = row[0].strip(), row[1].strip()
            refined_author = re.sub(r'^[^A-Za-z]+', '', author_name)
            if refined_author:
                uid_author_map[refined_author] = uid

# Load author names and IDs from the second CSV
name_id_map = {}
with open(name_id_csv, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader, None)  # Skip header
    for row in reader:
        if row:
            author_name, author_id = row[0].strip(), row[1].strip()
            refined_author = re.sub(r'^[^A-Za-z]+', '', author_name)
            if refined_author:
                name_id_map[refined_author] = author_id

# Merge and write results to the output CSV
with open(output_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Author Name", "Author ID", "UID"])  # Write header
    for author_name in sorted(uid_author_map.keys()):
        uid = uid_author_map[author_name]
        author_id = name_id_map.get(author_name, "N/A")  # Default to N/A if not found
        writer.writerow([author_name, author_id, uid])

print(f"Merged data has been saved to {output_csv}.")