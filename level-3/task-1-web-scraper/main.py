import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://quotes.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for quote in soup.find_all('span', class_='text')[:5]:
        print('-', quote.text)

if __name__ == '__main__':
    main()
