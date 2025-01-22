import csv

# Input and output file paths
input_csv = "cu_title_authors.csv"  # Replace with your CSV file name
output_csv = "cu_unique_authors_with_ids.csv"

# Set to track unique authors
unique_authors = set()

# Read the input CSV and extract authors
with open(input_csv, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if "Authors" in row:  # Ensure the column header exists
            authors = row["Authors"].split(",")  # Split authors by comma
            unique_authors.update(author.strip() for author in authors)
        else:
            raise KeyError("The input CSV file must have a 'Authors' column header.")

# Write unique authors with IDs to the output CSV
with open(output_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Author Name", "Author ID"])  # Write header
    for author in sorted(unique_authors):  # Sort authors alphabetically
        author_id = f"BUET_{author.replace(' ', '_')}"  # Create unique ID
        writer.writerow([author, author_id])

print(f"Unique authors with IDs have been saved to {output_csv}.")
