import csv

# Input and output file paths
input_csv = "_title_authors_BUET.csv"  # Replace with your input CSV file name
output_authors_csv = "_authors_with_ids_BUET.csv"
output_papers_csv = "_papers_with_ids_BUET.csv"

# Initialize counters and storage
author_counter = 0
paper_counter = 0
author_ids = {}
paper_ids = {}

# Read the input CSV and process data
with open(input_csv, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)  
    authors_output = []
    papers_output = []

    for row in reader:
        # Assign a unique paper ID
        paper_id = f"buet_paper_{paper_counter}"
        paper_counter += 1

        # Split authors and process each
        authors = [author.strip() for author in row["Authors"].split(",")]
        for author in authors:
            if author not in author_ids:
                # Assign a unique author ID
                author_id = f"buet_author_{author_counter}"
                author_counter += 1
                author_ids[author] = author_id
                # Add author to the authors_output list
                authors_output.append([author, author_id])
            
            # Add paper details to papers_output
            papers_output.append([author_ids[author], paper_id, row["Title"], author])  # Added author name

# Write authors to authors_with_ids.csv
with open(output_authors_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Author Name", "Author ID"])  # Header row
    writer.writerows(authors_output)

# Write papers to papers_with_ids.csv
with open(output_papers_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Author ID", "Paper ID", "Title", "Author Name"])  # Header row with Author Name
    writer.writerows(papers_output)

print(f"Authors have been saved to {output_authors_csv}.")
print(f"Papers have been saved to {output_papers_csv}.")