from bs4 import BeautifulSoup
import requests

# before scraping a website goto root url and add robots.txt to check what is allowed or not

response = requests.get(url="https://news.ycombinator.com/news", verify= False)
contents = response.text
# print(response.text)

soup = BeautifulSoup(contents, 'html.parser')

titles = soup.select(selector=".titleline a")
# print(titles[0].get("href"))
article_text = []
article_links = []
for article in titles:
    text = article.getText()
    article_text.append(text)

    links = article.get('href')
    article_links.append(links)


article_upvote = [int(upvote.getText().split()[0]) for upvote in soup.find_all(name= 'span', class_ = 'score')]
# print(article_upvote)
# print(article_links)
# print(article_text)
highest_upvote = article_upvote.index(max(article_upvote))
print(article_text[highest_upvote])
print(article_links[highest_upvote])