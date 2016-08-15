
import config
import random


#####################################################################################
###                            Class CreateFirstLevel                             ###
#####################################################################################

class CreateFirstLevel():

    def __init__(self):

        self.levelMap = []

        for x in range(config.numOfLevels):
            self.makeLevel()
            self.levelMap.append(self.tiltNewLevel)

    def makeLevel(self):
        self.blankLevel = [[' ' for y in range(config.fullLevelMap_Y)] for x in range(config.fullLevelMap_X)]
        self.createWalls()
        self.createPaths()
        self.createBorder()
        self.tiltNewLevelFunc()
        #createItems()
        #recompileLevel()


    def tiltNewLevelFunc(self):
        self.tiltNewLevel = [['' for y in range(config.fullLevelMap_Y+60)] for x in range(config.fullLevelMap_X+60)]
        for x in range(config.fullLevelMap_X):
            for y in range(config.fullLevelMap_Y):
                self.tiltNewLevel[y+30][x+30] = self.blankLevel[y][x]


    def firstLevel(self):
        pass

    def createBorder(self):
        for x in range(config.fullLevelMap_X):
            for y in range(config.fullLevelMap_Y):
                if x == 0 or y == 0 or x == config.fullLevelMap_X-1 or y == config.fullLevelMap_Y-1:
                    self.blankLevel[y][x] = config.WALLS["WALL_ALONE"]

    def createWalls(self):

        while True:

            len_room_x = random.randint(10,21)
            len_room_y = random.randint(10,21)

            rand_location_on_map_x = random.randint(0,config.fullLevelMap_X-1)
            rand_location_on_map_y = random.randint(0,config.fullLevelMap_Y-1)

            col = False
            for y in range(config.fullLevelMap_Y):
                if ' ' in self.blankLevel[y]: col = True

            if col:
                while self.blankLevel[rand_location_on_map_y][rand_location_on_map_x] != ' ':
                      while ' ' not in self.blankLevel[rand_location_on_map_y]:
                          rand_location_on_map_y = (rand_location_on_map_y + 1) % config.fullLevelMap_Y
                      rand_location_on_map_x = (rand_location_on_map_x + 1) % config.fullLevelMap_X

                for y in range(len_room_y):
                    for x in range(len_room_x):
                        if x == 0 or y == 0 or x == len_room_x-1 or y == len_room_y-1:
                            self.blankLevel[(y+rand_location_on_map_y)%config.fullLevelMap_Y][(x+rand_location_on_map_x)%config.fullLevelMap_X] = config.WALLS["WALL_ALONE"]
                        else:
                            self.blankLevel[(y+rand_location_on_map_y)%config.fullLevelMap_Y][(x+rand_location_on_map_x)%config.fullLevelMap_X] = config.OTHER_ICONS["FREE_SPACE"]
            else: break


    def createPaths(self):
        num_of_paths_X = config.fullLevelMap_X/10
        num_of_paths_Y = config.fullLevelMap_Y/10

        for x in range(int(num_of_paths_X)):
            place = random.randint(x*10+1, x*10+9)
            i = 0
            while i < config.fullLevelMap_Y:
                self.blankLevel[i][place] = '`'
                chance = random.randint(0, 10)
                if chance < 2 and place != 1:
                    place -= 1
                if chance > 8 and place != config.fullLevelMap_X-1:
                    place += 1
                else:
                    i += 1

        for y in range(int(num_of_paths_Y)):
            place = random.randint(y*10+1, y*10+9)
            i = 0
            while i < config.fullLevelMap_X:
                self.blankLevel[place][i] = '`'
                chance = random.randint(0, 10)
                if chance < 2 and place != 0:
                    place -= 1
                if chance > 8 and place != config.fullLevelMap_Y-1:
                    place += 1
                else:
                    i += 1

    def recompileLevel(self):
        pass

