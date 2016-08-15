__author__ = 'n7701-00-091'

import config
from game.createLevel import CreateFirstLevel

class movementLogic():

    def __init__(self):

        self.X = (config.fullLevelMap_X + config.X_CONST * 6) // 2
        self.Y = (config.fullLevelMap_Y + config.Y_CONST * 6) // 2
        self.caveMap = [[],[]]
        self.curentFloor = 0
        self.newLevels = [[],[],[]]

    def moveLeft(self):
        self.X -= 1
        for y in range(config.Y_CONST):
            self.caveMap[y] = self.caveMap[y][:-1]
            self.caveMap[y].insert(0, self.newLevels[self.curentFloor][self.Y + y][self.X])

    def moveRight(self):
        self.X += 1
        for y in range(config.Y_CONST):
            self.caveMap[y] = self.caveMap[y][1:]
            self.caveMap[y].append(self.newLevels[self.curentFloor][self.Y + y][self.X + config.X_CONST])

    def moveDown(self):
        for y in range(config.Y_CONST - 1):
            self.caveMap[y] = self.caveMap[y + 1]
        self.Y += 1
        self.caveMap[config.Y_CONST - 1] = self.newLevels[self.curentFloor][self.Y + config.Y_CONST][
                                                       self.X:self.X + config.X_CONST]

    def moveUp(self):
        for y in range(config.Y_CONST - 1):
            self.caveMap[config.Y_CONST - y - 1] = self.caveMap[config.Y_CONST - y - 2]
        self.Y -= 1
        self.caveMap[0] = self.newLevels[self.curentFloor][self.Y + 1][self.X:self.X + config.X_CONST]
