import csv
import re

# Input and output file paths
input_csv = "enhanced_unique_authors.csv"  # Input CSV: Author Name, Author ID, UID, Affiliation
output_csv = "enhanced_authors_with_enumerated_uids.csv"  # Output CSV

# Helper function to refine author names by removing prefixes and selecting the longest substring
def get_largest_substring(name):
    # Remove any leading non-alphabet characters
    name = re.sub(r'^[^A-Za-z]+', '', name)
    # Split by spaces and select the longest component
    parts = name.split()
    return max(parts, key=len) if parts else ""

# Dictionary to track enumerated UIDs for unique author names
author_uid_map = {}

# Process input CSV and generate unique integer UIDs
with open(input_csv, "r", encoding="utf-8") as infile, open(output_csv, "w", newline="", encoding="utf-8") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(reader, None)  # Read header

    if header:
        writer.writerow(["Author Name", "Author ID", "UID"])  # Write header

    current_uid = 1
    for row in reader:
        if row:
            author_name, author_id, uid = row[:3]
            refined_name = get_largest_substring(author_name.strip())

            if refined_name not in author_uid_map:
                author_uid_map[refined_name] = current_uid
                current_uid += 1

            writer.writerow([refined_name, author_id, author_uid_map[refined_name]])

print(f"Authors with enumerated integer UIDs have been saved to {output_csv}.")
