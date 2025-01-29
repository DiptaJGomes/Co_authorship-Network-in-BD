import csv
import re

# Input and output file paths
input_csv = "unique_authors.csv"  # Replace with your input file path
output_csv = "enumerated_authors.csv"

# Set to track unique authors
unique_authors = set()

# Read the input CSV and extract author names
with open(input_csv, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader, None)  # Skip the header row
    for row in reader:
        if row:  # Ensure row is not empty
            author = row[0].strip()  # Only consider the first column
            # Remove characters before the first alphabet in the name
            refined_author = re.sub(r'^[^A-Za-z]+', '', author)
            if refined_author:
                unique_authors.add(refined_author)

# Write unique authors with integer enumerated IDs to the output CSV
with open(output_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Author ID", "Author Name"])  # Write header
    for index, author in enumerate(sorted(unique_authors), start=1):
        writer.writerow([index, author])

print(f"Enumerated authors have been saved to {output_csv}.")