# Created on : 3/26/2021
# Created by : Joshua (Hong) Yoon
# main file for Hackathon project

import pygame
from game import Game
#from game.py file, import the Game class

pygame.init()

game = Game()
# delcare game as new object variable of Game(). No 'new' keyword required

game.run_game_loop()

pygame.quit()
quit()