from bs4 import BeautifulSoup
import requests
import time
response = requests.get("https://news.ycombinator.com/newest")
yc_webpage=response.text

soup= BeautifulSoup(yc_webpage, "html.parser")
# print(soup.prettify())
soup_body= soup.body
# print(soup_body)
my_data =soup_body.find_all(name="span", class_="titleline")
# print(my_data)

# for item in my_data:
    # print(item)
    # print(item.a)


my_titles = [item.getText() for item in my_data]

my_links =[item.a for item in my_data]


my_score= soup_body.find_all(name="span", class_="score")
my_scoores = [int(item.getText().split()[0]) for item in my_score]


num= my_scoores.index(max(my_scoores))


print(my_titles[num])
print(my_links[num])
print(my_scoores[num])

