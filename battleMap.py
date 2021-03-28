# Created on : 3/27/2021
# Created by : Joshua (Hong) Yoon
# battle map file for Hackathon project

import pygame
from battleMapTile import BattleMapTile
from playerCharacter import PlayerCharacter

class BattleMap:
    def __init__(self):
        self.window_width = 810
        self.window_height = 810
        self.window_coordinates = (0,0)

        self.battle_window = pygame.display.set_mode((self.window_width, self.window_height))

        self.clock2 = pygame.time.Clock()

        self.width = 80
        self.height = 80
        self.margin = 1
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.battle_grid = []

        self.tile = pygame.image.load('assets\\battleTile.png')
        self.image = pygame.transform.scale(self.tile, (self.width, self.height))


    def draw_battlefield(self):
        for row in range (10):
            self.battle_grid.append([])
            for column in range(10):
                self.battle_grid[row].append(0)
                # 0 is placeholder

    def visibility(self, character):
        for members in character.crew:
            self.member = pygame.image.load(member.attributes.image_path)
            self.member_image = pygame.transform.scake(self.member, (self.width, self.height))


    def battlelines(self, i):
        self.load_game = open(r'savefiles\\savegame' + str(i) + r'.txt', 'r')
        self.friendly = self.load_game.read()

        self.battle_files = open(r'temp\\info.txt', 'r')
        self.hostiles = self.load_game.read()

        for members in self.friendly:
            for column in range(0,0):
                for row in range(10):
                    if self.battle_grid[row] != 0:
                        continue
                    members.coordinates = (row, 0)

        for members in self.hostiles:
            for column in range(9,9):
                for row in range(10):
                    if self.battle_grid[row] != 0:
                        continue
                    members.coordinates = (row, 9)

    def move(self, player):
        movement_available = player.attributes.movement
        while movement_available <=0:
            self.move_vertical(player, movement_available)
            self.move_horizaontal(player,movement_available)

    def move_vertical(self, character, movement_available):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                user_input = pygame.mouse.get_pos()
                column = user_input[0] // (self.width + self.margin)
                row = user_input[1] // (self.height + self.margin)
                if column > character.coordinates[0] and character.coordinates[0] == self.battle_grid[column] and (character.coordinates[0] + 1) == 0:
                    character.coordinates[0] += 1
                    self.battle_grid[character.coordinates[0]][character.coordinates[1]] = 1
                    self.battle_grid[character.coordinates[0] - 1][character.coordinates[1]] = 0
                    return movement_available - 1
                elif column < character.coordinates[0] and character.coordinates[0] != 0 and (character.coordinates[0] -1) == 0:
                    character.coordinates[0] -= 1
                    self.battle_grid[character.coordinates[0]][character.coordinates[1]] = 1
                    self.battle_grid[character.coordinates[0] + 1][character.coordinates[1]] = 0
                    return movement_available - 1

    def move_horizontal(self, character, movement_available):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                user_input = pygame.mouse.get_pos()
                column = user_input[0] // (self.width + self.margin)
                row = user_input[1] // (self.height + self.margin)
                if row > character.coordinates[1] and character.coordinates[1] != 9 and (character.coordinates[1] + 1) == 0:
                    character.coordinates[1] += 1
                    self.battle_grid[character.coordinates[0]][character.coordinates[1] + 1] = 0
                    return movement_available - 1
                elif row < character.coordinates[1] and character.coordinates[1] != 0 and (character.coordinates[1] -1) == 0:
                    character.coordinates[1] -= 1
                    self.battle_grid[character.coordinates[0]][character.coordinates[1] - 1] = 0
                    return movement_available - 1

    def run_battle_loop(self):
        save_game = open(r'savefiles\\most_recent.txt', 'r')
        i = int(save_game.read(1))
        self.draw_battlefield()
        self.battlelines(i)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        event.type = pygame.QUIT


            self.battle_window.fill(self.black)

            self.visibility()

            for row in range(10):
                for column in range(10):
                    tile_location = pygame.draw.rect(self.battle_window, self.white, [(self.margin + self.width) * column + self.margin, (self.margin + self.height) * row + self.margin, self.width, self.height])
                    self.battle_window.blit(self.image, tile_location)

            pygame.display.update()

            self.clock2.tick(30)
        save_game.close()
        self.battle_files.close()
        self.load_game.close()
