import os
import warnings

import guiCreateMarkov
from markovchain import JsonStorage
from markovchain.text import MarkovText, ReplyMode

from guiDownloadLyrics import chartSwitcher

# Suppress reg. exp. warning that shows when using markovchain library
warnings.simplefilter(action='ignore', category=FutureWarning)

markovDir = "Markov"
markovScript = "markov.py"

def main(chart):

    selectedChart = chartSwitcher(chart)

    try:
        markov = MarkovText.from_file('%s/%s.json' % (markovDir, selectedChart))
    except FileNotFoundError:
        print("%s.json file not found. Using markov.py to create one first!" %
              selectedChart)
        guiCreateMarkov.create_directory()
        guiCreateMarkov.main(chart)
        markov = MarkovText.from_file('%s/%s.json' % (markovDir, selectedChart))

    print(markov())