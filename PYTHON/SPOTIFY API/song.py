from bs4 import BeautifulSoup
import requests
temp_url="https://www.billboard.com/charts/hot-100/$/"
class Song():
    def __init__(self):
        self.list=[]
    def _100songs(self,user):
        url=temp_url.replace('$',user)
        received=requests.get(url)
        data=received.text
        soup=BeautifulSoup(data,"html.parser")
        song_list=soup.select(selector="#title-of-a-story.c-title.a-no-trucate")
        self.list=[i.getText().strip() for i in song_list]
        return self.list
