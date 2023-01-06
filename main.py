import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')

url = 'https://edition.cnn.com/europe/live-news/russia-ukraine-war-news-1-6-23/index.html'

article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')


analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'Sentiment: {"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}')