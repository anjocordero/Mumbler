import os
import warnings

import guiCreateMarkov
import markovify

from guiDownloadLyrics import chartSwitcher

# Suppress reg. exp. warning that shows when using markovchain library
# warnings.simplefilter(action='ignore', category=FutureWarning)

markovDir = "Markov"
markovScript = "markov.py"

def main(chart):

    selectedChart = chartSwitcher(chart)

    try:
        with open('%s/%s.json' % (markovDir, selectedChart)) as file:
            markov = markovify.NewlineText.from_json(file.read())
            print(markov.make_sentence())
    except FileNotFoundError:
        print("%s.json file not found." %
              selectedChart)
        
    return