# Created on : 3/26/2021
# Created by : Joshua (Hong) Yoon
# main game file for Hackathon project
# See README.txt for asset credits

import pygame

import random
from gameCharacter import GameCharacter
from door import Door
from enemy import Enemy
from newLevel import NewLevel
from playerCharacter import PlayerCharacter

class Game:
    def __init__(self):
        self.window_width = 1600
        self.window_height = 800
        # arbitrary screen size, works best in personal laptop
        self.midpoint_width = int(self.window_width/2)
        self.midpoint_height = int(self.window_height/2)

        self.standard_width = 100
        self.standard_height = 100
        # standardized size for all objects (with exceptions)
        self.door_height = 50

        self.player_coordinates = (100, 400)
        # player starting location
        self.player_speed = 2
        self.enemy_speed = 1
        # arbitrary start speed

        self.player_offset = 200

        self.level = 1
        # determine level of difficulty of current room

        self.can_teleport = True
        self.is_hit = False
    
        self.window_coordinates = (0,0)
        self.clock = pygame.time.Clock()
        self.start = pygame.time.get_ticks()
        #for teleport cooldown
        self.start2 = pygame.time.get_ticks()
        #for on hit invulnerability
        self.player_health = 10
        self.enemy_health = 2

        self.game_window = pygame.display.set_mode((self.window_width, self.window_height))

        self.background = GameCharacter(self.window_coordinates[0], self.window_coordinates[1], self.window_width, self.window_height, 'assets\\layer1.jpg', 0)
        # used gameCharacter to not have to code an object for background
        self.doors = [
            Door(self.midpoint_width, 0, self.standard_width, self.door_height, 'assets\\door.png', 0)
        ]

        self.newLevel= NewLevel(self.window_width, self.window_height, self.doors[0])

        self.player = PlayerCharacter(self.player_coordinates[0], self.player_coordinates[1], self.standard_width, self.standard_height, 'assets\\mainPlayer.png' ,self.player_speed, self.player_health)

        self.enemy = Enemy(0, 0, self.standard_width, self.standard_height, 'assets\\enemy1.png', self.enemy_speed, self.enemy_health)
        self.enemies = [
            self.enemy
        ]
        # starting enemy, tutorial of sorts

        self.player_hitbox = pygame.Rect(self.player_coordinates[0], self.player_coordinates[1], self.standard_width, self.standard_height)
        i = 0
        self.enemy_hitbox_list = []
        for enemy in self.enemies:
            enemy_hitbox = pygame.Rect(enemy.x, enemy.y, self.standard_width, self.standard_height)
            self.enemy_hitbox_list.insert(i, enemy_hitbox)
            i += 1 
        i = 0
        self.door_hitbox_list = []
        for door in self.doors:
            door_hitbox = pygame.Rect(door.x, door.y, self.standard_width, self.door_height)
            self.door_hitbox_list.insert(i, door_hitbox)
            i += 1
        
    def draw_game(self):
        self.game_window.fill((255,255,255))
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        for enemy in self.enemies:
            if enemy == None:
                return
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))
        for door in self.doors:
            if door == None:
                return
            self.game_window.blit(door.image, (door.x, door.y))
        pygame.display.update()

    """ def redraw_game(self, enemies, doors):

        self.game_window.fill((255,255,255))
        #clear old drawing

        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        
        for enemy in enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))
        for door in doors:
            self.game_window.blit(door.image, (door.x, door.y))
        pygame.display.update() """

    def collision(self, player_hitbox, object_1):
        if player_hitbox.colliderect(object_1):
            return True
        else:
            return False
    
    def collision_consequence(self):
        if self.is_hit == False:
            i = 0
            for enemy_hitbox in self.enemy_hitbox_list:
                if self.collision(self.player_hitbox, enemy_hitbox):
                    self.is_hit = True
                    self.start = pygame.time.get_ticks()

                    if self.enemies[i].speed_y <= 0:
                        self.enemies[i].speed_y = abs(self.enemies[i].speed_y)
                    elif self.enemies[i].speed_y >= self.window_height - self.enemies[i].height:
                        self.enemies[i].speed_y = -self.enemies[i].speed_y
                    if self.enemies[i].speed_x <= 0:
                        self.enemies[i].speed_x = abs(self.enemies[i].speed_x)
                    elif self.enemies[i].speed_x >= self.window_width - self.enemies[i].width:
                        self.enemies[i].speed_x = -self.enemies[i].speed_x
                    if self.player_direction_y < 0:
                        self.player_direction_y = 1

                    elif self.player_direction_y > 0:
                        self.player_direction_y = -1

                    if self.player_direction_x < 0:
                        self.player_direction_x = 1

                    elif self.player_direction_x > 0:
                        self.player_direction_x = -1

                    i += 1
                    return 2

            for door_hitbox in self.door_hitbox_list:
                if self.collision(self.player_hitbox, door_hitbox):
                    self.is_hit = True
                    if(door_hitbox.x == self.midpoint_width and door_hitbox.y == self.midpoint_height):
                        self.level += 1
                        self.list_1 = self.newLevel.player_right(self.level)
                        self.player.x = self.player_offset
                        self.player.y = self.midpoint_height

                    elif(door_hitbox.x == 0 and door_hitbox.y == self.midpoint_height):
                        self.level += 1
                        self.list_1 = self.newLevel.player_left(self.level)
                        self.player.x = int(self.window_width - door_hitbox.width - self.player_offset)
                        self.player.y = self.midpoint_height

                    elif(door_hitbox.x == int(self.midpoint_width - self.standard_width) and door_hitbox.y == self.window_height - self.door_height):
                        self.level += 1
                        self.list_1 = self.newLevel.player_bottom(self.level)
                        self.player.x = self.midpoint_width
                        self.player.y = self.player_offset - 100

                    elif(door_hitbox.x == int(self.midpoint_width - self.standard_width) and door_hitbox.y == 0):
                        # see newLevel.py line 44 for reason of elif
                        self.level += 1
                        self.list_1 = self.newLevel.player_top(self.level)
                        self.player.x = self.midpoint_width
                        self.player.y = self.window_height - self.player_offset

                    i = 0                  
                    while i != self.list_1[0]:
                        n = random.randint(100, 1300)
                        if (n >= self.player.x and n <= int(self.player.x + self.player.width)):
                            n += self.player_offset
                        m = random.randint(100, 500)
                        if (m >= self.player.y and m <= int(self.player.y + self.player.height)):
                            m += self.player_offset
                        # prevent enemies spawning on top of player

                        enemy = Enemy(n, m, self.standard_width, self.standard_height, 'assets\\enemy1.png', self.enemy_speed, self.enemy_health)
                        self.enemies.insert(i, enemy)
                        i += 1
                    self.doors = self.list_1[1]

                    self.enemy_hitbox_list = []
                    for enemy in self.enemies:
                        self.enemy_hitbox_list.insert(i, pygame.Rect(enemy.x, enemy.y, self.standard_width, self.standard_height))
                        i += 1 
                    i = 0
                    self.door_hitbox_list = []
                    for door in self.doors:
                        self.door_hitbox_list.insert(i, pygame.Rect(door.x, door.y, self.standard_width, self.door_height))
                        i += 1
                    return 1
                else:
                    return 0
        
        else:
            return 0  

    def move_characters(self, direction_x, direction_y):
        self.player.moveHorizontal(direction_x, self.window_width)
        self.player.moveVertical(direction_y, self.window_height)
        for enemy in self.enemies:
            enemy.move(self.window_height, self.window_width)

        self.player_hitbox[0] = self.player.x
        self.player_hitbox[1] = self.player.y

        i = 0
        for enemy in self.enemies:
            self.enemy_hitbox_list[i].x = enemy.x
            self.enemy_hitbox_list[i].y = enemy.y
            i += 1 
        i = 0

    def teleport(self):
        if(self.player_direction_x !=0 and self.player_direction_y != 0 and self.can_teleport == True):
            self.player.teleport_horizontal(self.player_direction_x, self.window_width)
            self.player.teleport_vertical(self.player_direction_y, self.window_height)
            self.can_teleport = False
            self.start = pygame.time.get_ticks()                  

        elif(self.player_direction_x != 0 and self.can_teleport == True):
            self.player.teleport_horizontal(self.player_direction_x, self.window_width)
            self.can_teleport = False
            self.start = pygame.time.get_ticks()
            
        elif(self.player_direction_y != 0 and self.can_teleport == True):
            self.player.teleport_vertical(self.player_direction_y, self.window_height)
            self.can_teleport = False
            self.start = pygame.time.get_ticks()
            
    def events_key_down(self, event):
        if event.key == pygame.K_w:
            self.player_direction_y = -1
            return self.player_direction_y
        elif event.key == pygame.K_s:
            self.player_direction_y = 1
            return self.player_direction_y
        elif event.key == pygame.K_d:
            self.player_direction_x = 1
            return self.player_direction_x
        elif event.key == pygame.K_a:
            self.player_direction_x = -1
            return self.player_direction_x
        elif event.key == pygame.K_ESCAPE:
            event.key = pygame.QUIT
        elif event.key == pygame.K_q:
            self.teleport()

    def events_key_up(self, event):
        if event.key == pygame.K_w or event.key == pygame.K_s:
            self.player_direction_y = 0
            return self.player_direction_y
        elif event.key == pygame.K_d or event.key == pygame.K_a:
            self.player_direction_x = 0
            return self.player_direction_x

    # Constantly looping and running for event handling
    def run_game_loop(self):
        self.player_direction_x = 0
        self.player_direction_y = 0
        self.draw_game()

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    self.events_key_down(event)
                elif event.type == pygame.KEYUP:
                    self.events_key_up(event)
            
            end = pygame.time.get_ticks()
            if (end - self.start >= 5000):
                self.can_teleport = True
            if (end - self.start2 >= 2000):
                self.is_hit = False

            self.move_characters(self.player_direction_x, self.player_direction_y)
            self.draw_game()

            if self.collision_consequence() == 0:
                continue
            elif self.collision_consequence() == 1:
                self.draw_game()
            elif self.collision_consequence() == 2:
                if self.player_health >= 1:
                    self.player_health -= 1
                else:
                    return
            self.clock.tick(30)