#!/usr/bin/env python3

from phrasehunter.game import Game
from phrases import PHRASES



if __name__ == '__main__': 
   game = Game(PHRASES) 
   game.start()
