from bs4 import BeautifulSoup
import requests

url = "https://example.com"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

for row in soup.find_all('tr'):
    cols = row.find_all('td')
    print([col.text.strip() for col in cols])
