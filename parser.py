from bs4 import BeautifulSoup
from song import Song
import requests

page = requests.get('https://www.billboard.com/charts/hot-100')
soup = BeautifulSoup(page.content, 'html.parser')
titles = soup.find_all(class_='chart-list-item__title-text')
titles.insert(0, soup.find(class_='chart-number-one__title'))
artists = soup.find_all(class_='chart-list-item__artist')
artists.insert(0, soup.find(class_='chart-number-one__artist'))

SongList = []

if len(titles) == len(artists):

    for title, artist in zip(titles, artists):
        song = Song()
        song.title = title.get_text(strip=True)
        song.artist = artist.get_text(strip=True)
        SongList.append(song)

else:
    print("Mismatch in song titles and artists. Exiting.")
    exit()

for song in SongList:
    print(song.title + ", " + song.artist)