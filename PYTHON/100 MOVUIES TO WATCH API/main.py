import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

received=requests.get(URL)
data=received.text
soup=BeautifulSoup(data,"html.parser")
all_title=soup.select(class_="title",selector="h3")
movie_list=[]
for i in all_title:
        (movie_list.append(i.getText()))
movie_list=movie_list[::-1]
for i,k in enumerate(movie_list):
    with open("data.txt","a",encoding="utf-8") as file:
        file.write(f"{k}\n")


