import csv
import re
from difflib import SequenceMatcher

# Input file paths
uid_author_csv = "enumerated_authors.csv"  # First CSV: UID and Author Name
name_id_csv = "merged_author_id.csv"  # Second CSV: Author Name and Author ID
output_csv = "unique_authors.csv"  # Output CSV

# Load UID and author names from the first CSV
uid_author_map = {}
with open(uid_author_csv, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader, None)  # Skip header
    for row in reader:
        if row:
            uid, author_name = row[0].strip(), row[1].strip()
            refined_author = re.sub(r'^[^A-Za-z]+', '', author_name)
            if refined_author and refined_author.count(' ') <= 4:
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
            if refined_author and refined_author.count(' ') <= 4:
                name_id_map[refined_author] = author_id

# Helper function to check if two names match based on an 8-character substring
def names_match(name1, name2):
    return SequenceMatcher(None, name1.lower(), name2.lower()).find_longest_match(0, len(name1), 0, len(name2)).size >= 8

# Merge authors and ensure unique UID
merged_authors = []
used_uids = set()

for author_name, uid in uid_author_map.items():
    if uid not in used_uids:
        merged_authors.append((author_name, name_id_map.get(author_name, "N/A"), uid))
        used_uids.add(uid)

for author_name, author_id in name_id_map.items():
    found_match = False
    for existing_author, _, uid in merged_authors:
        if names_match(author_name, existing_author):
            found_match = True
            break
    if not found_match:
        # Assign a new UID if no match found
        new_uid = f"UID_{len(used_uids) + 1}"
        merged_authors.append((author_name, author_id, new_uid))
        used_uids.add(new_uid)

# Write merged unique authors to the output CSV
with open(output_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Author Name", "Author ID", "UID"])  # Write header
    for author_name, author_id, uid in merged_authors:
        writer.writerow([author_name, author_id, uid])

print(f"Merged unique authors with substring matching and unique UIDs have been saved to {output_csv}.")