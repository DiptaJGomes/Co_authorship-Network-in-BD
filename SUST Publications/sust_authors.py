import csv
import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://www.sust.edu/d/cse/research'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Lists to store data
    authors_list = []
    titles = []

    # Locate each <p> tag with publications
    publications = soup.select('p')
    
    for pub in publications:
        # Find all titles in <strong> tags within <p> elements
        strong_tags = pub.find_all('strong')
        if len(strong_tags) > 1:
            # The first <strong> tag is the topic; the rest are titles
            for title_tag in strong_tags[1:]:
                title = title_tag.get_text(strip=True)
                
                # Extract author text up to the title
                author_text = pub.get_text(strip=True).split(title)[0].strip()
                
                # Append authors and title to lists
                authors_list.append(author_text)
                titles.append(title)

    # Save to CSV
    with open('sust_authorlist.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Authors', 'Title'])  # Write headers
        writer.writerows(zip(authors_list, titles))

    print("Data saved to sust_authorlist.csv")
else:
    print("Failed to retrieve the page")
