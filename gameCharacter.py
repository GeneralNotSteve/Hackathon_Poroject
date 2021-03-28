# Created on : 3/26/2021
# Created by : Joshua (Hong) Yoon
# game character file for Hackathon project

import pygame

class GameCharacter:
    def __init__ (self, x, y, width, height, image_path, speed):
        image = pygame.image.load(image_path)

        self.image = pygame.transform.scale(image, (width, height))
        # size will be standardized

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
