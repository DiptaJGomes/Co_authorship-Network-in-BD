import csv
import re

# Input and output file paths
input_csv = "_authors_with_ids_BUET.csv"  # Replace with your input CSV path
output_csv = "updated_authors_with_ids_BUET.csv"

# Read the input CSV and modify author IDs
rows = []
with open(input_csv, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header
    for row in reader:
        if row:
            author_name, author_id = row[0], row[1]
            # Replace "brac_" with "buet_" in the author ID
            new_author_id = author_id.replace("brac_", "buet_")
            rows.append([author_name, new_author_id])

# Write the modified data to the new CSV
with open(output_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write header
    writer.writerows(rows)  # Write updated rows

print(f"Updated author IDs have been saved to {output_csv}.")
