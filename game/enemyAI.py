__author__ = 'n7701-00-091'

import config
import random
from game.movementModul import MovementLogic


class EnemyMovement():

    def __init__(self):
        self.movement = 1
        self.complexity_logic = 1
        self.level_map = []
        self.enemy_location = []
        self.movementLogic = MovementLogic()
        self.new_levels = [[], [], []]
        self.x_position = self.z_position = self.y_position = self.horizontal_move = self.vertical_move = 0

    def put_enemies(self):
        rand_x = rand_y = 5
        if self.level_map:
            for z in range(config.numOfLevels):
                for x in range(100):
                    while self.level_map[z][rand_y][rand_x] != config.OTHER_ICONS["FREE_SPACE"]:
                        rand_x = random.randint(5, config.fullLevelMap_X + (config.X_CONST * 6) - 5)
                        rand_y = random.randint(5, config.fullLevelMap_Y + (config.Y_CONST * 6) - 5)
                    self.level_map[z][rand_y][rand_x] = config.OTHER_ICONS["ENEMY"]
                    self.enemy_location += [[z, rand_y, rand_x]]

    def enemy_check_direction(self):
        if self.level_map:
            for x in range(len(self.enemy_location)):
                self.x_position = self.enemy_location[x][2]
                self.y_position = self.enemy_location[x][1]
                self.z_position = self.enemy_location[x][0]
                self.horizontal_move = random.randint(-1, 1)
                self.vertical_move = random.randint(-1, 1)
                if self.vertical_move != 0:
                    if self.vertical_move == -1 and self.level_map[self.z_position][self.y_position - 1][self.x_position] == config.OTHER_ICONS["FREE_SPACE"]:
                            self.level_map[self.z_position][self.y_position - 1][self.x_position] = config.OTHER_ICONS["ENEMY"]
                            self.level_map[self.z_position][self.y_position][self.x_position] = config.OTHER_ICONS["FREE_SPACE"]
                            self.enemy_location[x][1] -= 1
                    elif self.vertical_move == 1 and self.level_map[self.z_position][self.y_position + 1][self.x_position] == config.OTHER_ICONS["FREE_SPACE"]:
                            self.level_map[self.z_position][self.y_position + 1][self.x_position] = config.OTHER_ICONS["ENEMY"]
                            self.level_map[self.z_position][self.y_position][self.x_position] = config.OTHER_ICONS["FREE_SPACE"]
                            self.enemy_location[x][1] += 1
                elif self.horizontal_move != 0:
                    if self.horizontal_move == -1 and self.level_map[self.z_position][self.y_position][self.x_position - 1] == config.OTHER_ICONS["FREE_SPACE"]:
                            self.level_map[self.z_position][self.y_position][self.x_position - 1] = config.OTHER_ICONS["ENEMY"]
                            self.level_map[self.z_position][self.y_position][self.x_position] = config.OTHER_ICONS["FREE_SPACE"]
                            self.enemy_location[x][2] -= 1
                    if self.horizontal_move == 1 and self.level_map[self.z_position][self.y_position][self.x_position + 1] == config.OTHER_ICONS["FREE_SPACE"]:
                            self.level_map[self.z_position][self.y_position][self.x_position + 1] = config.OTHER_ICONS["ENEMY"]
                            self.level_map[self.z_position][self.y_position][self.x_position] = config.OTHER_ICONS["FREE_SPACE"]
                            self.enemy_location[x][2] += 1
