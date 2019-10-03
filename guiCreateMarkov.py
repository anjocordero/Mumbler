import os
from os import path
import warnings

import markovify

from chart import chartSwitcher
from config import lyricDirectory

markovDir = "Markov" 

# Suppress reg. exp. warning that shows when using markovchain library
# warnings.simplefilter(action='ignore', category=FutureWarning)

def create_directory():
    """Creates directory for .json markovchain databases"""

    # Create directory for all lyrics
    try:
        os.mkdir(markovDir)
    except FileExistsError:
        pass


def main(chart):

    create_directory()

    rootDir = chartSwitcher(chart)

    text = []

    print("Updating " + chart + " Markov Chain")

    # Remove .json if it already exists
    if path.exists('%s/%s.json' % (markovDir, rootDir)):
        os.remove('%s/%s.json' % (markovDir, rootDir))

    # Iterate through folders in selected genre
    for dirName, subdirList, fileList in os.walk(lyricDirectory + "/" + rootDir):

        # Ignore hidden directories like .git
        exclude_prefixes = ('__', '.')

        # prevent os.walk from traversing hidden directories
        # [:] slice operator makes changes in place so they affects os.walk
        subdirList[:] = [
            d for d in subdirList if not d.startswith(exclude_prefixes)]

        fileList = [f for f in fileList if not f.startswith(exclude_prefixes)]

        # For each artist in chosen directory
        # split functions accomodate both linux/mac and windows
        print("Found artist: " + dirName.split("/")
              [len(dirName.split("/")) - 1].split("\\")[len(dirName.split("\\")) - 1])

        # For each song by artist
        for fname in fileList:

            with open(dirName + "/" + fname) as fp:
                for line in fp:
                    if not line.startswith("["):
                        text.append(line)
                        #markov.data(line, part=False)

            print("\tAdded song: " + fname)

        # Close data with space?
        # Unsure if necessary, was included in markovchain documentation
        # markov.data('', part=False)

        # print statements not functional as is
        # print(markov())
        # print(markov(max_length=16, reply_to='sentence start',
        #              reply_mode=ReplyMode.END))

        #markov.save('%s/%s.json' % (markovDir, rootDir))

    markov = markovify.NewlineText(text)

    with open('%s/%s.json' % (markovDir, rootDir), 'w+') as file:
        file.write(markov.to_json())
    
    print("Markov chain build complete!")