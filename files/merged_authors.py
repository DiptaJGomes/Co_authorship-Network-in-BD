import csv
import os

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
                    unique_authors.add(author)

# Write unique authors to the output CSV
with open(output_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Author Name"])  # Write header
    for author in sorted(unique_authors):  # Sort authors alphabetically
        if author:  # Ensure non-empty author names
            writer.writerow([author])

print(f"Unique authors have been saved to {output_csv}.")