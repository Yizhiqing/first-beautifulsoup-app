import requests
from bs4 import BeautifulSoup

page = requests.get("http://www.sohu.com")
soup = BeautifulSoup(page.content, 'html.parser')
items = soup.find_all("a")
for item in items:
    print(item)
