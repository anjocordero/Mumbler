# Mumbler

Procedurally generate lyrics based on Billboard top songs.
Allows the user to choose between the Hot 100, Pop, Latin, EDM, Rock, Alternative, 
and R&B/Hip-Hop charts.
Scrapes the songs + artists off of Billboard's website, then uses googlesearch
to download the lyrics of each song on azlyrics.com.

Current usage:

Run main.py through the command line:
`python3 main.py` 

This launches a basic tkinter GUI which lets you choose which Billboard genre
you want to use, along with options to either download or generate
lyrics.

## Dependencies

* python3

* googlesearch

  + install using `pip3 install google` 
  + installing this first likely will download BeautifulSoup as a dependency

* Beautiful Soup 4

  + install using `pip3 install beautifulsoup4` 

* markovify
  + install using `pip3 install markovify` 

Known Issues:

* Currently times out when searching for lyrics, possibly sending too many requests
  + Remedied by only allowing 10 searches at once then stopping

* Currently incompatible with Billboard's Hot 100 chart, since the HTML structure is different than the rest of their charts.

* Performing an action, then switching genres and downloading lyrics seems to download lyrics into the wrong genre's folder

