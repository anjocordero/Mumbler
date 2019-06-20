import os

from markovchain import JsonStorage
from markovchain.text import MarkovText, ReplyMode

from parser import chartSwitcher, lyricDirectory


def main():

    rootDir = chartSwitcher()
    markov = MarkovText()

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
                    markov.data(line, part=False)

            print("\tAdded song: " + fname)

        # Close data with space?
        # Unsure if necessary, was included in markovchain documentation
        markov.data('', part=False)

        print(markov())
        print(markov(max_length=16, reply_to='sentence start',
                     reply_mode=ReplyMode.END))

        markov.save('%s.json' % (rootDir))

        markov = MarkovText.from_file('markov.json')


if __name__ == '__main__':
    main()
