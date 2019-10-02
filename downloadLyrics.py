import os.path
import sys
from os import path

import requests
from bs4 import BeautifulSoup
from googlesearch import search

from song import Song

# Global variables to store song details
SongList = []
titles = []
artists = []

# To prevent being blocked from too many google requests
# not sure what the max number actually is
searchMax = 10
searchEnd = 0

# Name of directory containing song lyrics
lyricDirectory = "Lyrics"

# Variables to find lyrics when scraping azlyrics.com
# Found through html on azlyrics page for a specific song
azlyricsClass = "col-xs-12 col-lg-8 text-center"
azlyricsDivNumber = 6


def chartSwitcher():
    """
    Choose which billboard chart to search, when given argument in command line

    chartName taken from billboard.com urls
    """

    if len(sys.argv) > 1:
        chart = sys.argv[1]
    else:
        chart = None

    if chart == "hot100":
        chartName = "hot-100"

    elif chart == "pop":
        chartName = "pop-songs"

    elif chart == "latin":
        chartName = "latin-songs"

    elif chart == "hiphop":
        chartName = "r-b-hip-hop-songs"

    elif chart == "edm":
        chartName = "dance-electronic-songs"

    elif chart == "alternative":
        chartName = "alternative-songs"

    elif chart == "rock":
        chartName = "rock-songs"

    else:
        print(
            "No genre specified. Try again with [hot100/pop/rock/latin/hiphop/alternative/edm].")
        exit(1)

    return chartName


def create_directory():
    """Creates directory to store song lyrics"""

    # Create directory for all lyrics
    try:
        os.mkdir(lyricDirectory)
    except FileExistsError:
        pass

    # Create directory for specific billboard chart
    try:
        os.mkdir(lyricDirectory + "/" + chartSwitcher())
    except FileExistsError:
        pass


def read_billboard(chartName):
    """
    Read top song titles and artists from billboard

    TODO: - Add azlyrics search functionality for less reliance on google
            - current function can run as backup when azlyrics search returns no results
                - this happens when features are inconsistent across titles
          - reimplement hot100 functionality after billboard.com layout change
    """

    page = requests.get('https://www.billboard.com/charts/' + chartName)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Add artists and titles to list

    
    if chartSwitcher() == 'hot100':
        #element_class = 'chart-element__information'
        print("hot100 functionality currently unavailable! Try another genre")
        return
    else:
        element_class = 'chart-list-item'

    # TODO: Add compatibility with hot100 chart hierarchy, old method doesn't work as of 9/25/19 

    for list_item in soup.find_all(class_=element_class):
        titles.append(list_item['data-title'].replace("/", " "))
        artists.append(list_item['data-artist'].replace("/", " "))

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
            os.mkdir(lyricDirectory + "/" +
                     chartSwitcher() + "/" + song.artist)
        except FileExistsError:
            pass

        # Check if lyric file already exists for this song
        if path.exists(lyricDirectory + "/" + chartSwitcher() + "/" + song.artist + "/" + song.title):
            song.downloaded = True


def write_lyrics(song):
    """Writes a single song's lyrics to a file, separating lines by newlines"""

    # ./lyricDirectory/Chart/Artist/Song
    try:
        with open(lyricDirectory + "/" + chartSwitcher() + "/" + song.artist + "/" + song.title, 'w') as fh:
            fh.writelines("%s\n" % line for line in song.lyrics)
            print("Wrote " + song.title + " by " + song.artist)
    except FileExistsError:
        print(song.title + " file already exists.")


def find_lyrics():
    """Search azlyrics for song lyrics and add to database"""

    # Create counter to prevent being blocked from google searches
    searchNum = 0
    searchEnd = 0

    for song in SongList:

        if not song.downloaded:

            # Break to prevent being blocked from google searches
            if searchNum == searchMax:
                searchEnd = 1
                break

            # Google search for song on azlyrics
            url = list(search(song.title + ' ' + song.artist +
                              ' azlyrics.com', stop=1))[0]
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            text = soup.find(class_=azlyricsClass)

            searchNum += 1

            if text:
                lyrics = text.find_all('div')[azlyricsDivNumber]
                song.lyrics = list(lyrics.stripped_strings)

            else:
                song.lyrics = []

            write_lyrics(song)

    if searchEnd == 0:
        print("All " + chartSwitcher() + " lyrics downloaded.")
    else:
        print("Reached search max, quitting for now. Run this again in a few minutes to continue updating.")


if __name__ == '__main__':
    chartName = chartSwitcher()
    create_directory()
    read_billboard(chartName)
    check_database()
    find_lyrics()
