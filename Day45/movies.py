from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url= URL, verify= False)
contents = response.text

# print(contents)
soup = BeautifulSoup(contents, 'html.parser')

titles = soup.find_all(name= 'h3', class_ = 'title')
# print(titles[-1].getText().split())

with open('movies.txt','w', encoding= 'utf-8') as file:
    for movie in titles[::-1]:
        title_text = movie.getText().replace(')', '.')
        
        file.write(title_text + '\n')
    