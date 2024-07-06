from bs4 import BeautifulSoup


with open('website.html', encoding= 'utf-8') as fp:
    contents = fp.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title.name)    # return the name of the tag
# print(soup.title)  # returns the whole tag
# print(soup.title.contents) # returns the list of things inside the tag
# print(soup.title.string)  # returns the string inside the tag

# print(soup.prettify())   # returns the whole html code with pretty format

# print(soup.a) # return the first anchor tag
all_anchor_tags = soup.find_all(name= "a")   # you can write the name of tag which you want like p for paragraph
# print(all_anchor_tags)
# print(soup.find(name='h1')) # gives the first h1 tag
# print(soup.find(name='h1', id = 'name'))  # gives the specific h1 tag with given id

# print(soup.find( class_ = 'heading'))    # gives the element with this class, if two classes are there with the same name it will return only the first occurence
# for tag in all_anchor_tags:
#     print(tag.get("href"))  # gives the url inside href
#     print(tag.getText())  # gives the text inside the anchor tags

company_url = soup.select_one(selector="p a") # to select a particular tag here the a tag is inside p tag
# print(company_url)

name = soup.select_one(selector="#name") # you can also use ids and class in selector
# print(name)

# select all with a particular class
headings = soup.select(selector=".heading")
# print(headings)