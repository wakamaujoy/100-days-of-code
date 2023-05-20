from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
best_movies=response.text

soup = BeautifulSoup(best_movies, "html.parser")
# print(soup.prettify())
all_movies= soup.find_all(name="div", class_="jsx-4245974604 listicle-item-image")
# text = [item.getText() for item in all_movies]

print(all_movies)
# print(text)

