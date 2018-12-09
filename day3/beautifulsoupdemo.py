from bs4 import BeautifulSoup
import requests

r = requests.get('http://python.org')

data = r.content

soup = BeautifulSoup(data, 'html.parser')

for link in soup.find_all('a', class_="jump-to-menu"):
    print(link.get('href'))

print(soup.children[2])
