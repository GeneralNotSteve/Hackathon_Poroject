# Created on : 3/26/2021
# Created by : Joshua (Hong) Yoon
# level creation file for Hackathon project

import pygame
import random
from door import Door
class NewLevel:

    def __init__(self, width, height, door):

        self.width = width
        self.height = height
        self.door = door
        self.midpoint_width = int(self.width/2)
        self.midpoint_height = int(self.height/2)
        self.standard_width = 100
        self.standard_height = 100
        self.door_height = int(self.standard_height /2)
        self.doors = []

    def random_door_generator(self, n, door_i, doors):
        if n >= 10 and n < 20:
            if door_i.x == 0 and door_i.y == self.midpoint_height:
                door2 = Door(int(self.width - standard_width), self.midpoint_height, self.standard_width, self.door_height, 'assets\\door.png', 0)
                self.doors.append(door2)
            else:
                door2 = Door(0, self.midpoint_height, self.standard_width, self.door_height, 'assets\\door.png', 0)
                self.doors.append(door2)
        elif n >= 20 and n < 30:
            if door_i.x == int(self.width - self.standard_width) and door_i.y == self.midpoint_height:
                door2 = Door(self.midpoint_width, int(self.height - door.height), self.standard_width, self.door_height, 'assets\\door.png', 0)
                self.doors.append(door2)
            else:
                door2 = Door(int(self.width - self.standard_width), self.midpoint_height, self.standard_width, self.door_height, 'assets\\door.png', 0)
                self.doors.append(door2)
        elif n >=30 and n <=50:
            if door_i.x == 0 and door_i.y == self.midpoint_height:
                door2 = Door(int(self.width - standard_width), self.midpoint_height, self.standard_width, self.door_height, 'assets\\door.png', 0)
                self.door3 = Door(self.midpoint_width, int(self.height - door.height), self.standard_width, self.door_height, 'assets\\door.png', 0)
                self.doors.append(door2)
                self.doors.append(self.doors3)

            elif door_i.x == int(self.width - self.standard_width) and door_i.y == self.midpoint_height:
                door2 = Door(self.midpoint_width, int(self.height - door.height), self.standard_width, self.door_height, 'assets\\door.png', 0)
                self.door3 = Door(self.midpoint_width, 0, self.standard_width, self.door_height, 'assets\\door.png', 0)
                self.doors.append(door2)
                self.doors.append(self.doors3)

            elif door_i.x == self.midpoint_width and door_i.y == int(self.height - door.height):
                door2 = Door(0, self.midpoint_height, self.standard_width, self.door_height, 'assets\\door.png', 0)
                self.door3 = Door(int(self.width - self.standard.width), self.midpoint_height, self.standard_width, self.door_height, 'assets\\door.png', 0)
                self.doors.append(door2)
                self.doors.append(self.doors3)

            elif door_i.x == self.midpoint_width and door_i.y == 0:
                # not else statement for purposes of off-centered door additions
                door2 = Door(int(self.width - self.standard.width), self.midpoint_height, self.standard_width, self.door_height, 'assets\\door.png', 0)
                self.door3 = Door(self.midpoint_width, int(self.height - door.height), self.standard_width, self.door_height, 'assets\\door.png', 0)
                self.door4 = Door(0, self.midpoint_height, self.standard_width, self.door_height, 'assets\\door.png', 0)
                self.doors.append(door2)
                self.doors.append(self.doors3)
                self.doors.append(self.doors4)
        return

    def player_right(self, level):
    # player enters level from right side (next room they are left hand side)
        i = random.randint(10, 50)
        door = Door(0, self.midpoint_height, self.standard_width, self.door_height, 'assets\\door.png', 0)
        self.doors.append(door)
        self.random_door_generator(i, self.door, self.doors)
        return [random.randint(1, level), self.doors]

    def player_left(self, level):
    # player enters level from left side (next room they are right hand side)
        i = random.randint(10, 50)
        door = Door(int(self.width - standard_width), self.midpoint_height, self.standard_width, self.door_height, 'assets\\door.png', 0)
        self.doors.append(door)
        self.random_door_generator(i, self.door, self.doors)
        return [random.randint(1, level), self.doors]

    def player_top(self, level):
    # player enters level from top (next room they are bottom)
        i = random.randint(10, 50)
        door = Door(self.midpoint_width, int(self.height - self.door.height), self.standard_width, self.door_height, 'assets\\door.png', 0)
        self.doors.append(door)
        self.random_door_generator(i, self.door, self.doors)
        return [random.randint(1, level), self.doors]

    def player_bottom(self, level):
    # player enters level from bottom (next room they are top)
        i = random.randint(10, 50)
        door = Door(self.midpoint_width, 0, self.standard_width, self.door_height, 'assets\\door.png', 0)
        self.doors.append(door)
        self.random_door_generator(i, self.door, self.doors)
        return [random.randint(1, level), self.doors]
