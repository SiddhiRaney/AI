from newspaper import Article

url = 'https://www.bbc.com/news/world-us-canada-68870145'
article = Article(url)

article.download()         # Step 1: Download HTML
article.parse()            # Step 2: Parse content
article.nlp()              # Step 3: Optional - NLP for summary, keywords

print("Title:", article.title)
print("Authors:", article.authors)
print("Published Date:", article.publish_date)
print("Summary:", article.summary)
print("Text:", article.text[:500])  # Only showing first 500 chars


from newspaper import Article

url = 'https://www.nytimes.com/2024/04/05/world/europe/france-retirement-age.html'
article = Article(url)

article.download()
article.parse()
article.nlp()

print("Title:", article.title)
print("Authors:", article.authors)
print("Published Date:", article.publish_date)
print("Summary:", article.summary)
print("Text:", article.text[:500])


from newspaper import Article

url = 'https://edition.cnn.com/2023/11/03/tech/twitter-x-advertising/index.html'
article = Article(url)

article.download()
article.parse()
article.nlp()

print("Title:", article.title)
print("Authors:", article.authors)
print("Published Date:", article.publish_date)
print("Summary:", article.summary)
print("Text:", article.text[:500])
