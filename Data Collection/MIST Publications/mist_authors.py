import requests
from bs4 import BeautifulSoup
import csv

# URL of the research list page
url = "https://bup.edu.bd/research-list"

# Send an HTTP request to fetch the page content
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all research titles and corresponding links
research_items = soup.find_all('div', class_='col-md-12 mb-4')

# Initialize a list to store the research data
research_data = []

# Loop through each research item and extract the title and URL
for item in research_items:
    # Extract the research title and link
    title_tag = item.find('h3').find('a')
    title = title_tag.get_text(strip=True)
    link = title_tag['href']
    
    # Follow the link to the detailed research page
    if link.startswith("http"):
        research_url = link  # It's already a full URL
    else:
        research_url = f"https://bup.edu.bd{link}"  # Append to the base URL
    
    research_response = requests.get(research_url)
    research_response.raise_for_status()
    
    # Parse the detailed research page
    research_soup = BeautifulSoup(research_response.content, 'html.parser')
    
    # Extract the authors (assuming they are in a specific tag, like <p> or <span>)
    authors = research_soup.find('div', class_='author-info')  # Adjust the class if necessary
    if authors:
        authors = authors.get_text(strip=True)
    else:
        authors = "Authors not found"
    
    # Store the research title, URL, and authors
    research_data.append({'title': title, 'url': research_url, 'authors': authors})

# Save the research data to a CSV file
csv_filename = 'research_data.csv'
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'url', 'authors'])
    writer.writeheader()  # Write the header row
    writer.writerows(research_data)  # Write all research data rows

print(f"Data has been saved to {csv_filename}")

# Optionally print the research data
for research in research_data:
    print(f"Title: {research['title']}")
    print(f"URL: {research['url']}")
    print(f"Authors: {research['authors']}")
    print('-' * 80)
