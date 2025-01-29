import csv
import os
import re

# Directory containing the input CSV files
input_directory = "./Authors"  # Replace with your directory
output_csv = "unique_authors.csv"

# Set to track unique authors
unique_authors = set()

# Loop through all CSV files in the directory
for filename in os.listdir(input_directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_directory, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header row
            for row in reader:
                if row:  # Ensure row is not empty
                    author = row[0].strip()  # Only consider the first column
                    # Remove characters before the first alphabet in the name
                    refined_author = re.sub(r'^[^A-Za-z]+', '', author)
                    if refined_author:
                        unique_authors.add(refined_author)

# Write unique authors to the output CSV
with open(output_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Author Name"])  # Write header
    for author in sorted(unique_authors):  # Sort authors alphabetically
        writer.writerow([author])

print(f"Unique authors have been saved to {output_csv}.")