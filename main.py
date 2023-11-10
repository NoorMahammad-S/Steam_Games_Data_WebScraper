import requests
from bs4 import BeautifulSoup
import csv

# URL of the Steam website with the games you want to scrape
url = "https://store.steampowered.com/search/?filter=topsellers"

# Send a GET request to the Steam URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the section containing game information
games_section = soup.find('div', {'id': 'search_resultsRows'})

# Create a CSV file to store the scraped data
csv_filename = "steam_games.csv"

# Open the CSV file for writing with UTF-8 encoding
with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    # Write the header row
    writer.writerow(["Title", "Price", "User Rating"])

    # Find and write data rows
    game_elements = games_section.find_all('a', {'class': 'search_result_row'})
    for game_element in game_elements:
        title = game_element.find('span', {'class': 'title'}).text.strip() if game_element.find('span', {'class': 'title'}) else "N/A"
        price = game_element.find('div', {'class': 'search_price'}).text.strip() if game_element.find('div', {'class': 'search_price'}) else "N/A"
        user_rating = game_element.find('span', {'class': 'search_review_summary'}).get('data-tooltip-html') if game_element.find('span', {'class': 'search_review_summary'}) else "N/A"

        writer.writerow([title, price, user_rating])

print(f"Scraped Steam game data and saved to {csv_filename}")
