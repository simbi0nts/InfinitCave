__author__ = 'n7701-00-091'

import config


class MovementLogic():

    def __init__(self):
        self.X = (config.fullLevelMap_X + config.X_CONST * 6) // 2
        self.Y = (config.fullLevelMap_Y + config.Y_CONST * 6) // 2
        self.cave_map = [[], []]
        self.current_floor = 0
        self.new_levels = [[], [], []]

    def move_left(self):
        self.X -= 1
        for y in range(config.Y_CONST):
            self.cave_map[y] = self.cave_map[y][:-1]
            self.cave_map[y].insert(0, self.new_levels[self.current_floor][self.Y + y][self.X])

    def move_right(self):
        self.X += 1
        for y in range(config.Y_CONST):
            self.cave_map[y] = self.cave_map[y][1:]
            self.cave_map[y].append(self.new_levels[self.current_floor][self.Y + y][self.X + config.X_CONST])

    def move_down(self):
        for y in range(config.Y_CONST - 1):
            self.cave_map[y] = self.cave_map[y + 1]
        self.Y += 1
        self.cave_map[config.Y_CONST - 1] = self.new_levels[self.current_floor][self.Y + config.Y_CONST][self.X:self.X + config.X_CONST]

    def move_up(self):
        for y in range(config.Y_CONST - 1):
            self.cave_map[config.Y_CONST - y - 1] = self.cave_map[config.Y_CONST - y - 2]
        self.Y -= 1
        self.cave_map[0] = self.new_levels[self.current_floor][self.Y + 1][self.X:self.X + config.X_CONST]
