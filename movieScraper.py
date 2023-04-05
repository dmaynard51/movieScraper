import requests
from bs4 import BeautifulSoup

# Specify the URL of the Rotten Tomatoes website
url = 'https://www.rottentomatoes.com/top/bestofrt/'

# Send a GET request to the website and retrieve the HTML content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the list of movies in the HTML using the appropriate class or HTML tags
movies = soup.find_all(class_='js-tile-link')
for movie in movies:
    title = movie.find('span', class_='p--small', attrs={'data-qa': 'discovery-media-list-item-title'})
    rating = movie.find('score-pairs')
    audienceScore =  (rating['audiencescore'])
    criticScore =  (rating['criticsscore'])
    print ("Movie Title: ", title.text.strip(), "Audience Score: ", audienceScore, "Critic Score: ", criticScore)
