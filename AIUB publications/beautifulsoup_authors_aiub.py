import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the AIUB publications page
url = 'https://www.aiub.edu/publications'  # Replace with the actual page URL

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Lists to store the extracted data
    authors_list = []
    titles = []
    
    # Find each publication card and extract relevant information
    for card in soup.find_all('div', class_='card mb-3'):
        # Extract author names if present
        author_tag = card.find('small', class_='text-muted text-capitalize')
        authors = author_tag.get_text(strip=True) if author_tag else "N/A"
        
        # Extract publication title if present
        title_tag = card.find('a')
        title = title_tag.get_text(strip=True) if title_tag else "N/A"
        
        # Append data to lists
        authors_list.append(authors)
        titles.append(title)
    
    # Create a DataFrame
    data = pd.DataFrame({
        'Authors': authors_list,
        'Title': titles
    })
    
    # Save to CSV
    data.to_csv('aiub_authors_and_publications.csv', index=False)
    print("Data saved to aiub_authors_and_publications.csv")
else:
    print("Failed to retrieve the page")
