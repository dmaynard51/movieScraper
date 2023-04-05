Web Scraping Movie Ratings from Rotten Tomatoes

This is a Python web scraping application that retrieves movie ratings from Rotten Tomatoes website using the BeautifulSoup library. It extracts the audience score and other relevant information from HTML snippets and stores them in a format of your choice (e.g., CSV, JSON, etc.) for further analysis.
Features

    Retrieves movie ratings from Rotten Tomatoes website.
    Extracts audience score and other relevant information from HTML snippets.
    Supports processing a list of HTML snippets in a loop.
    Stores extracted data in a format of your choice (e.g., CSV, JSON, etc.) for further analysis.

Usage

    Clone the repository to your local machine.

bash

git clone https://github.com/your-username/movie-ratings-web-scraper.git

    Install the required dependencies.

pip install beautifulsoup4

    Run the web_scraper.py script.

python web_scraper.py

    Modify the html_list variable in the script to include the HTML snippets that you want to process.

python

# List of HTML snippets to process
html_list = [
    '<span class="p--small" data-qa="discovery-media-list-item-title">Shazam!</span>',
    '<span class="p--small" data-qa="discovery-media-list-item-title">Avengers: Endgame</span>',
    '<span class="p--small" data-qa="discovery-media-list-item-title">Spider-Man: Into the Spider-Verse</span>'
]

    The extracted data will be stored in a format of your choice (e.g., CSV, JSON, etc.) in the specified output file.

Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. You can also raise issues for bug reports or feature requests.
License

This project is licensed under the MIT License.
Credits

This project was developed by Daniel Maynard
