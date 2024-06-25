import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://www.kiss.cz/kissparada/"

current_day = datetime.now()
current_day = current_day.strftime("%d-%m-%Y")

response = requests.get(url=URL)
web_html = response.text

soup = BeautifulSoup(web_html, "html.parser")

songs = soup.find_all(class_="event clear-fix")
song_total = []
for song in songs:
    interpreter = song.find(class_="interpret").getText()
    song_name = song.find(class_="eventEvent eventKP pull-left").contents[-1].strip()
    song_finish = interpreter, song_name
    with open(f"kissparada-{current_day}.txt", mode="a", encoding="utf-8") as data:
        data.write(f"{interpreter} - {song_name}\n")
    
    
    
    
#     song_total.extend([song_finish])
# print(song_total[0][1])
 


# song_rank = song.find(class_="eventTime eventKP pull-left")
# song_rank = song_rank.getText().strip()

