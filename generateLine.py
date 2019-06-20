import os
import warnings
from downloadLyrics import chartSwitcher

import createMarkov
from markovchain import JsonStorage
from markovchain.text import MarkovText, ReplyMode

# Suppress reg. exp. warning that shows when using markovchain library
warnings.simplefilter(action='ignore', category=FutureWarning)

markovDir = "Markov"
markovScript = "markov.py"

def main():

    selectedChart = chartSwitcher()

    try:
        markov = MarkovText.from_file('%s/%s.json' % (markovDir, selectedChart))
    except FileNotFoundError:
        print("%s.json file not found. Using markov.py to create one first!" %
              selectedChart)
        createMarkov.create_directory()
        createMarkov.main()
        markov = MarkovText.from_file('%s/%s.json' % (markovDir, selectedChart))

    print(markov())


if __name__ == '__main__':
    main()
