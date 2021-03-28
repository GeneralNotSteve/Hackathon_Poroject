# Created on : 3/26/2021
# Created by : Joshua (Hong) Yoon
# door asset file for Hackathon project

from gameCharacter import GameCharacter

class Door(GameCharacter):

    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path, speed)

        self.x = x - width
        if self.x < 0:
            self.x = 0