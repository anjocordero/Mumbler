import os
from os import path
import warnings

from markovchain import JsonStorage
from markovchain.text import MarkovText, ReplyMode

from downloadLyrics import chartSwitcher, lyricDirectory

markovDir = "Markov"
rootDir = chartSwitcher()

# Suppress reg. exp. warning that shows when using markovchain library
warnings.simplefilter(action='ignore', category=FutureWarning)

def create_directory():
    """Creates directory for .json markovchain databases"""

    # Create directory for all lyrics
    try:
        os.mkdir(markovDir)
    except FileExistsError:
        pass


def main():

    markov = MarkovText()

    # Remove .json if it already exists
    if path.exists('%s.json' % (rootDir)):
        os.remove('%s.json' % (rootDir))

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
        print("Found artist: " + dirName.split("/")
              [len(dirName.split("/")) - 1])

        # For each song by artist
        for fname in fileList:

            with open(dirName + "/" + fname) as fp:
                for line in fp:
                    if not line.startswith("["):
                        markov.data(line, part=True)

            print("\tAdded song: " + fname)

        # Close data with space?
        # Unsure if necessary, was included in markovchain documentation
        markov.data('', part=False)

        # print statements not functional as is
        # print(markov())
        # print(markov(max_length=16, reply_to='sentence start',
        #              reply_mode=ReplyMode.END))

        markov.save('%s/%s.json' % (markovDir, rootDir))


if __name__ == '__main__':
    create_directory()
    main()
