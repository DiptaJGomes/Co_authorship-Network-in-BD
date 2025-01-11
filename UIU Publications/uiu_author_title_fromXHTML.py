from bs4 import BeautifulSoup
import csv

# Load the HTML file
with open('UIU_research.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the content with BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Lists to store data
authors_list = []
titles_list = []

# Locate the relevant sections
papers = soup.find_all('div', class_='paper-details')

for paper in papers:
    # Extract the title
    title_tag = paper.find('h2', class_='paper-title')
    title = title_tag.text.strip() if title_tag else "N/A"
    
    # Extract the authors
    authors_tag = paper.find('p', class_='paper-contributors')
    authors = [author.text.strip() for author in authors_tag.find_all('span')] if authors_tag else []
    
    # Add to lists
    titles_list.append(title)
    authors_list.append(', '.join(authors))

# Save to CSV
with open('extracted_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Authors'])  # Headers
    for title, authors in zip(titles_list, authors_list):
        writer.writerow([title, authors])

print("Data successfully extracted and saved to extracted_data.csv")
