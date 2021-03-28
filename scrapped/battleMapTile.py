# Created on : 3/27/2021
# Created by : Joshua (Hong) Yoon
# battle map tile file for Hackathon project

import pygame

class BattleMapTile:
    def __init__(self, width, height, image_path):

        self.width = width
        self.height = height

        image = pygame.image.load(image_path)

        self.image = pygame.transform.scale(image, (width, height))