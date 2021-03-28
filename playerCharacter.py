# Created on : 3/27/2021
# Created by : Joshua (Hong) Yoon
# player character file for Hackathon project

import pygame
from gameCharacter import GameCharacter

class PlayerCharacter(GameCharacter):
    def __init__(self, x, y, width, height, image_path, speed, health_max):
        super().__init__(x, y, width, height, image_path, speed)

        self.teleport_distance = 300
        
    
    def moveVertical(self, direction, max_height):
        if (self.y >= max_height - self.height and direction > 0)  or (self.y <= 0 and direction < 0):
            return
        self.y += (direction * self.speed)

    def moveHorizontal(self, direction, max_width):
        if (self.x >= max_width - self.width and direction > 0) or (self.x <= 0 and direction < 0):
            return
        self.x += (direction * self.speed)


    def teleport_vertical(self, direction, max_height):
        if (self.y >= max_height - self.height and direction > 0) and (self.y + 150 >= max_height):
            self.y = max_height - self.height
            return
        elif (self.y- self.teleport_distance <= 0 and direction < 0):
            self.y = 0
        elif (direction >0):
            self.y += self.teleport_distance
        elif (direction < 0):
            self.y -= self.teleport_distance

    def teleport_horizontal(self, direction, max_width):
        if (self.x >= max_width - self.width and direction > 0) and (self.x + 150 >= max_width):
            self.x = max_width - self.width
            return
        elif (self.x- self.teleport_distance <= 0 and direction < 0):
            self.x = 0
            return
        elif (direction > 0):
            self.x += self.teleport_distance
            return
        elif (direction < 0):
            self.x -= self.teleport_distance
            return

