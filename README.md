# Steam Games Data WebScraper

This Python script scrapes information about the top-selling games on Steam and saves the data in a CSV file. 
It uses the `requests`, `BeautifulSoup`, and `csv` libraries to accomplish this task.

## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started, you can clone this repository or simply download the Python script and use it in your local environment.

### Prerequisites

Before using this script, ensure that you have the following dependencies installed:
- Python 3.x
- `requests` library
- `BeautifulSoup` library
- A text editor or integrated development environment (IDE) for Python

You can install the required Python libraries using pip:
```bash
pip install requests beautifulsoup4
```

### Installation

1. Clone this repository or download the Python script to your local machine.

2. Install the required libraries as mentioned in the prerequisites section.

## Usage

1. Open the Python script in your text editor or IDE.

2. Modify the `url` variable to specify the Steam URL you want to scrape. By default, it's set to the top sellers' page: `"https://store.steampowered.com/search/?filter=topsellers"`

3. Run the script to scrape the data and save it to a CSV file. The script will generate a CSV file named `steam_games.csv` in the same directory.

```python
python steam_game_scraper.py
```

4. The CSV file will contain the following columns: "Title," "Price," and "User Rating."

## Contributing

Contributions to this project are welcome. If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Disclaimer:** This script is intended for educational and personal use only. Please respect the terms of service and usage policies of the websites you scrape and ensure compliance with relevant laws and regulations.
