from bs4 import BeautifulSoup
import requests
import song

page = requests.get('https://www.billboard.com/charts/hot-100')
soup = BeautifulSoup(page.content, 'html.parser')
songs = soup.find_all(class_='chart-list-item__title-text')
songs.insert(0, soup.find(class_='chart-number-one__title'))
artists = soup.find_all(class_='chart-list-item__artist')
artists.insert(0, soup.find(class_='chart-number-one__artist'))
print([song.get_text(strip=True) for song in songs])
print([artist.get_text(strip=True) for artist in artists])