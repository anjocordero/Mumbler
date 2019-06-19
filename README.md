# Mumbler

Procedurally generate lyrics based on Billboard top songs.
Allows the user to choose between the Hot 100, Pop, Latin, and R&B/Hip-Hop charts.
Scrapes the songs + artists off of Billboard's website, then uses googlesearch
to download the lyrics of each song on azlyrics.com.

Current step: Inputting the lyrics into a Markov Chain.

## Dependencies

- python3

- googlesearch
  - install using `pip install google`

- Beautiful Soup 4
  - Check their documentation page for installation instructions

- markovchain
  - install using `pip install markovchain`

Known Issues:

- Currently times out when searching for lyrics, possibly sending too many requests
  - Being remedied by only allowing 10 searches at once
