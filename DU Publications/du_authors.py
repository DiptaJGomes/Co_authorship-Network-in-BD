import csv
import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://www.du.ac.bd/researchDetails/35"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Lists to store data
    authors_list = []
    titles = []

    # Locate each publication entry by finding the 'tr' tags
    publications = soup.find_all('tr')

    # Iterate over each publication
    for pub in publications:
        details = pub.find_all('td')
        if len(details) > 1:
            # Extract author (inside <u>) and title (inside <i>)
            author = details[1].find('u').get_text(strip=True) if details[1].find('u') else "N/A"
            title = details[1].find('i').get_text(strip=True) if details[1].find('i') else "N/A"
            authors_list.append(author)
            titles.append(title)

    # Save to CSV
    with open('publications.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Author', 'Title'])  # Write headers
        writer.writerows(zip(authors_list, titles))

    print("Data saved to publications.csv")
else:
    print("Failed to retrieve the page")
