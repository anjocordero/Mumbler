from bs4 import BeautifulSoup
from googlesearch import search
from song import Song
import os.path
from os import path
import requests
import time

# Global variables to store song details
SongList = []
titles = []
artists = []

# Name of directory containing song lyrics
directoryName = "Lyrics"

# Variables to find lyrics when scraping azlyrics.com
azlyricsClass = "col-xs-12 col-lg-8 text-center"
azlyricsDivNumber = 6


def create_directory():
    """Creates directory to store song lyrics"""

    try:
        os.mkdir(directoryName)
    except FileExistsError:
        pass


def read_billboard():
    """Read top song titles and artists from billboard"""

    page = requests.get('https://www.billboard.com/charts/hot-100')
    soup = BeautifulSoup(page.content, 'html.parser')

    # Add artists and titles to list

    for list_item in soup.find_all(class_='chart-list-item'):
        titles.append(list_item['data-title'])
        artists.append(list_item['data-artist'])

    # Check if data was read in correctly

    if len(titles) == len(artists) and len(titles) != 0:

        for title, artist in zip(titles, artists):
            song = Song()
            song.title = title
            song.artist = artist
            SongList.append(song)

    else:
        print("Billboard data not found. Exiting.")
        exit()


def check_database():
    """Checks if song lyrics are already downloaded"""

    for song in SongList:

        # Create folder for artist
        try:
            os.mkdir(directoryName + "/" + song.artist)
        except FileExistsError:
            pass

        # Check if lyric file already exists for this song
        if path.exists(directoryName + "/" + song.artist + "/" + song.title):
            song.downloaded = True


def write_lyrics(song):
    try:
        with open(directoryName + "/" + song.artist + "/" + song.title, 'w') as fh:
            fh.writelines("%s\n" % line for line in song.lyrics)
            print("Wrote " + song.title)
    except FileExistsError:
        print(song.title + " file already exists.")


def find_lyrics():
    """Search azlyrics for song lyrics and add to database"""

    # for song, i in zip(SongList, range(40)):
    for song in SongList:

        if not song.downloaded:
            # Google search for song on azlyrics
            url = list(search(song.title + ' ' + song.artist + ' azlyrics.com', stop=1))[0]
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            text = soup.find(class_=azlyricsClass)

            if text:
                lyrics = text.find_all('div')[azlyricsDivNumber]
                song.lyrics = list(lyrics.stripped_strings)

            else:
                song.lyrics = []

            write_lyrics(song)


if __name__ == '__main__':
    create_directory()
    read_billboard()
    check_database()
    find_lyrics()
