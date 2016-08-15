import config
import random

#################################################################################
#                            Class CreateFirstLevel                             #
#################################################################################


class CreateFirstLevel():
    def __init__(self):

        self.level_map = []
        self.tilt_new_level = []
        self.blank_level = []
        for x in range(config.numOfLevels):
            self.make_level()
            self.level_map.append(self.tilt_new_level)

    def make_level(self):
        self.blank_level = [[' ' for y in range(config.fullLevelMap_Y)] for x in range(config.fullLevelMap_X)]
        self.create_walls()
        self.create_paths()
        self.create_items()
        self.create_border()
        self.tilt_new_level_func()

    def tilt_new_level_func(self):
        self.tilt_new_level = [[config.WALLS["WALL_ALONE"] for x in range(config.fullLevelMap_X + (config.X_CONST * 6))]
                               for y in range(config.fullLevelMap_Y + (config.Y_CONST * 6))]
        for x in range(config.fullLevelMap_X):
            for y in range(config.fullLevelMap_Y):
                self.tilt_new_level[y + config.Y_CONST * 3][x + config.X_CONST * 3] = self.blank_level[y][x]

    def create_items(self):
        rand_x = rand_y = 5
        if self.level_map:
            for x in range(100):
                while self.blank_level[rand_y][rand_x] != config.OTHER_ICONS["FREE_SPACE"] and self.blank_level[rand_y][rand_x] not in config.WALLS.values():
                    rand_x = random.randint(5, config.fullLevelMap_X - 5)
                    rand_y = random.randint(5, config.fullLevelMap_Y - 5)
                self.blank_level[rand_y][rand_x] = config.OTHER_ICONS["LEVEL_DOWN"]
                self.level_map[len(self.level_map) - 1][rand_y + config.Y_CONST * 3][rand_x + config.X_CONST * 3] = config.OTHER_ICONS["LEVEL_UP"]
        for x in range(250):
            while self.blank_level[rand_y][rand_x] != config.OTHER_ICONS["FREE_SPACE"] and self.blank_level[rand_y][rand_x] not in config.WALLS.values():
                rand_x = random.randint(5, config.fullLevelMap_X - 5)
                rand_y = random.randint(5, config.fullLevelMap_Y - 5)
            self.blank_level[rand_y][rand_x] = config.OTHER_ICONS["ADDITIONAL_TIME"]

    def create_border(self):
        for x in range(config.fullLevelMap_X):
            for y in range(config.fullLevelMap_Y):
                if x == 0 or y == 0 or x == config.fullLevelMap_X - 1 or y == config.fullLevelMap_Y - 1:
                    self.blank_level[y][x] = config.WALLS["WALL_ALONE"]

    def create_walls(self):
        while True:
            len_room_x = random.randint(10, 21)
            len_room_y = random.randint(10, 21)
            rand_location_on_map_x = random.randint(0, config.fullLevelMap_X - 1)
            rand_location_on_map_y = random.randint(0, config.fullLevelMap_Y - 1)
            col = False
            for y in range(config.fullLevelMap_Y):
                if ' ' in self.blank_level[y]:
                    col = True
            if col:
                while self.blank_level[rand_location_on_map_y][rand_location_on_map_x] != ' ':
                    while ' ' not in self.blank_level[rand_location_on_map_y]:
                        rand_location_on_map_y = (rand_location_on_map_y + 1) % config.fullLevelMap_Y
                    rand_location_on_map_x = (rand_location_on_map_x + 1) % config.fullLevelMap_X
                for y in range(len_room_y):
                    for x in range(len_room_x):
                        if x == 0 or y == 0 or x == len_room_x - 1 or y == len_room_y - 1:
                            self.blank_level[(y + rand_location_on_map_y) % config.fullLevelMap_Y][
                                (x + rand_location_on_map_x) % config.fullLevelMap_X] = config.WALLS["WALL_ALONE"]
                        else:
                            self.blank_level[(y + rand_location_on_map_y) % config.fullLevelMap_Y][
                                (x + rand_location_on_map_x) % config.fullLevelMap_X] = config.OTHER_ICONS["FREE_SPACE"]
            else:
                break

    def create_paths(self):
        num_of_paths_x = config.fullLevelMap_X / 10
        num_of_paths_y = config.fullLevelMap_Y / 10
        for x in range(int(num_of_paths_x)):
            place = random.randint(x * 10 + 1, x * 10 + 9)
            i = 0
            while i < config.fullLevelMap_Y:
                self.blank_level[i][place] = '`'
                chance = random.randint(0, 10)
                if chance < 2 and place != 1:
                    place -= 1
                if chance > 8 and place != config.fullLevelMap_X - 1:
                    place += 1
                else:
                    i += 1
        for y in range(int(num_of_paths_y)):
            place = random.randint(y * 10 + 1, y * 10 + 9)
            i = 0
            while i < config.fullLevelMap_X:
                self.blank_level[place][i] = '`'
                chance = random.randint(0, 10)
                if chance < 2 and place != 0:
                    place -= 1
                if chance > 8 and place != config.fullLevelMap_Y - 1:
                    place += 1
                else:
                    i += 1