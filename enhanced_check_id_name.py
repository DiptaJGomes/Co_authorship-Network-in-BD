import csv
import re

# Input and output file paths
input_csv = "unique_authors.csv"  # Input CSV: Author Name, Author ID, UID
output_csv = "enhanced_unique_authors.csv"  # Output CSV

# Helper function to refine author names by removing prefixes and selecting the longest substring
def get_largest_substring(name):
    # Remove any leading non-alphabet characters
    name = re.sub(r'^[^A-Za-z]+', '', name)
    # Split by spaces and select the longest component
    parts = name.split()
    return max(parts, key=len) if parts else ""

# Process and write the refined author names to a new CSV
with open(input_csv, "r", encoding="utf-8") as infile, open(output_csv, "w", newline="", encoding="utf-8") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(reader, None)  # Read header

    if header:
        writer.writerow(["Author Name", "Author ID", "UID"])  # Write header

    for row in reader:
        if row:
            author_name, author_id, uid = row
            refined_name = get_largest_substring(author_name.strip())
            writer.writerow([refined_name, author_id, uid])

print(f"Enhanced unique authors have been saved to {output_csv}.")