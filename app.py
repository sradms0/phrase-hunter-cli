#!/usr/bin/env python3

'''Phrase Guessing Game

This script runs a singler player game, having the player guess a random phrase selected from a file. 

This script requires that a 'phrases.py' file is available within the same directory of this script. This file should contains an array of strings, but should already exist within the directory, upon cloning the reposistory
'''

from phrasehunter.game import Game
from phrases import PHRASES



if __name__ == '__main__': 
   game = Game(PHRASES) 
   game.start()
