import requests
from bs4 import BeautifulSoup

# --------------------------------------
# 1. Extract all links from a webpage
print("\n--- All Links ---")
url1 = "ADD_URL_HERE"
res1 = requests.get(url1)
soup1 = BeautifulSoup(res1.text, 'html.parser')
for link in soup1.find_all('a'):
    href = link.get('href')
    if href:
        print(href)

# --------------------------------------
# 2. Get all headings (h1, h2, h3)
print("\n--- All Headings ---")
url2 = "ADD_URL_HERE"
res2 = requests.get(url2)
soup2 = BeautifulSoup(res2.text, 'html.parser')
for heading in soup2.find_all(['h1', 'h2', 'h3']):
    print(f"{heading.name} --> {heading.text.strip()}")

# --------------------------------------
# 3. Scrape all paragraphs from a page
print("\n--- All Paragraphs ---")
url3 = "ADD_URL_HERE"
res3 = requests.get(url3)
soup3 = BeautifulSoup(res3.text, 'html.parser')
for para in soup3.find_all('p'):
    print(para.text.strip())

# --------------------------------------
# 4. Extract image URLs from a webpage
print("\n--- All Image URLs ---")
url4 = "ADD_URL_HERE"
res4 = requests.get(url4)
soup4 = BeautifulSoup(res4.text, 'html.parser')
for img in soup4.find_all('img'):
    src = img.get('src')
    if src:
        print(src)

# --------------------------------------
# 5. Get table data from a webpage
print("\n--- Table Data ---")
url5 = "ADD_URL_HERE"
res5 = requests.get(url5)
soup5 = BeautifulSoup(res5.text, 'html.parser')
table = soup5.find('table')
for row in table.find_all('tr'):
    cols = row.find_all('td')
    data = [col.text.strip() for col in cols]
    if data:
        print(data)
