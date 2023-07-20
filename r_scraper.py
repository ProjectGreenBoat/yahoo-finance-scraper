import requests
from bs4 import BeautifulSoup

def fetch_yahoo_articles():
	url = 'https://finance.yahoo.com/topic/stock-market-news'
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	# Find all li elements with class "js-stream-content"
	articles = soup.find_all('li', class_='js-stream-content')
	for article in articles:
		# print article details
		print(article.find('h3').text)
		print(article.find('a')['href'])
		print(article.find('p').text)
		print()

fetch_yahoo_articles()