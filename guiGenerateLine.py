import os
import warnings

import guiCreateMarkov
import markovify

from chart import chartSwitcher
from config import markovDir

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