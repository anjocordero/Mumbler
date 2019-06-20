import os
from markovchain import JsonStorage
from markovchain.text import MarkovText, ReplyMode
# from markovchain import JsonStorage
# from markovchain.text import MarkovText

def main():

    rootDir = '.'

    for dirName, subdirList, fileList in os.walk(rootDir):

        # Ignore hidden directories like .git
        exclude_prefixes = ('__', '.')

        fileList = [f for f in fileList if not f.startswith(exclude_prefixes)]

        # [:] slice operator to prevent os.walk from traversing hidden directories
        subdirList[:] = [d for d in subdirList if not d.startswith(exclude_prefixes)]

        # Search by artist
        print("Found artist: " + dirName.split("/")[len(dirName.split("/")) - 1])

        # For each song by artist
        for fname in fileList:
            print("\t" + fname)


if __name__ == '__main__':
    main()