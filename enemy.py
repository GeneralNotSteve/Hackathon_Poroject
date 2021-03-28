# Created on : 3/27/2021
# Created by : Joshua (Hong) Yoon
# enemy file for Hackathon project

from gameCharacter import GameCharacter

class Enemy(GameCharacter):
    def __init__ (self, x, y, width, height, image_path, speed, health_max):
        super().__init__(x, y, width, height, image_path, speed)

        self.speed_x = self.speed
        self.speed_y = self.speed
        # To bounce more interestingly

    def moveVertical(self, max_height):
        if self.y <= 0:
            self.speed_y = abs(self.speed_y)
            #abs(i) returns the absolute value of i
        elif self.y >= max_height - self.height:
            self.speed_y = -self.speed_y
        self.speed = self.speed_y
        self.y += self.speed_y

    def moveHorizontal(self, max_width):
        if self.x <= 0:
            self.speed_x = abs(self.speed_x)
        elif self.x >= max_width - self.width:
            self.speed_x = -self.speed_x
        self.speed = self.speed_x
        self.x += self.speed_x

    def move(self, max_height, max_width):
        self.moveHorizontal(max_width)
        self.moveVertical(max_height)


    