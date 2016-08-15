__author__ = 'n7701-00-091'

import config
from random import *
import os, math

class gameCore():

    def __init__(self):

        self.caveMap = [[config.OTHER_ICONS["FREE_SPACE"] for x in range(config.X_CONST)] for y in range(config.Y_CONST)]
        self.recompileMap = [[" " for x in range(config.X_CONST)] for y in range(config.Y_CONST)]
        self.startPosition()
        self.movePointsDone = 0
        self.movePointsLeft = 45
        self.movesToRemoveOneLightPoint = 10
        self.lightPoints = 0
        self.deletedSymb = config.OTHER_ICONS["FREE_SPACE"]
        self.voidArray = [config.OTHER_ICONS["FREE_SPACE"] for x in range(config.X_CONST)]


    def startPosition(self):
        self.caveMap[config.Y_CONST//2][config.X_CONST//2] = config.OTHER_ICONS["PLAYER"]


    def movePointIncremental(self):
        if self.deletedSymb == 'H':
            self.movePointsLeft += 5
            for i in range(3):
                if self.lightPoints > 0:
                    self.lightPoints -= 1
        else:
            self.movePointsLeft -= 1
            self.movesToRemoveOneLightPoint -= 1
        if self.movesToRemoveOneLightPoint == 0:
            self.lightPoints += 1
            self.movesToRemoveOneLightPoint = randint(4, 7)
        self.movePointsDone += 1


    def move(self, HorizontalMove, VerticalMove):

        if self.caveMap[(config.Y_CONST//2)+VerticalMove][config.X_CONST//2+HorizontalMove] not in config.WALLS.values():
            self.deletedSymb = self.caveMap[(config.Y_CONST//2)+VerticalMove][config.X_CONST//2+HorizontalMove]
            self.caveMap[config.Y_CONST//2][config.X_CONST//2] = config.OTHER_ICONS["FREE_SPACE"]
            if VerticalMove != 0:
                if VerticalMove == -1:
                    for y in range(config.Y_CONST-1):
                        self.caveMap[config.Y_CONST-y-1] = self.caveMap[config.Y_CONST-y-2]
                    self.caveMap[0] = [config.OTHER_ICONS["FREE_SPACE"] for x in range(config.X_CONST)]
                elif VerticalMove == 1:
                    for y in range(config.Y_CONST-1):
                        self.caveMap[y] = self.caveMap[y+1]
                    self.caveMap[config.Y_CONST-1] = [config.OTHER_ICONS["FREE_SPACE"] for x in range(config.X_CONST)]
            elif HorizontalMove != 0:
                for y in range(config.Y_CONST):
                    if HorizontalMove == -1:
                        self.caveMap[y] = self.caveMap[y][:-1]
                        self.caveMap[y].insert(0, config.OTHER_ICONS["FREE_SPACE"])
                    if HorizontalMove == 1:
                        self.caveMap[y] = self.caveMap[y][1:]
                        self.caveMap[y].append(config.OTHER_ICONS["FREE_SPACE"])
            self.startPosition()
            self.movePointIncremental()
        self.showCave()


    def doMessUp(self):

        someRandomIncremental = randint(1,10)
        for i in range(someRandomIncremental):
            freeSpaceLeft = 0
            inc = 0
            for y in range(config.Y_CONST):
                freeSpaceLeft += self.caveMap[y].count(config.OTHER_ICONS["FREE_SPACE"]) + self.caveMap[y].count(config.OTHER_ICONS["ADDITIONAL_TIME"])
            findElement = randint(0, freeSpaceLeft)
            hChance = randint(0, 15)
            for y in range(config.Y_CONST):
                for x in range(config.X_CONST):
                    if self.caveMap[y][x] == config.OTHER_ICONS["FREE_SPACE"] or self.caveMap[y][x] == config.OTHER_ICONS["ADDITIONAL_TIME"]:
                        if inc != findElement:
                            inc += 1
                        else:
                            if hChance == 1:
                                self.caveMap[y][x] = config.OTHER_ICONS["ADDITIONAL_TIME"]
                            else:
                                self.caveMap[y][x] = config.WALLS["WALL_CROSS"]
                            inc += 1
                            continue
        self.startPosition()


    def showCave(self):

        os.system('cls')
        self.doMessUp()
        print('\n\t\t\tMoves done: ' + str(self.movePointsDone))
        print('\t\t\tMoves left: ' + str(self.movePointsLeft) + '\n')
        self.recomLightMap(self.recompileMap, self.lightPoints)
        for y in range(config.Y_CONST):
            showStrLine = ''.join(self.recompileMap[y])
            print('\t\t' + showStrLine)


    def recomLightMap(self, recompileMap, radLight):

        vekt_y = (config.Y - 1) - radLight
        vekt_x = (config.X - 1) - radLight
        k_vekt_x = 1
        k_vekt_y = 1
        k_vekt = vekt_x
        if vekt_x < vekt_y:
            k_vekt_y = vekt_y/vekt_x
            k_vekt = vekt_y
        elif vekt_x > vekt_y:
            k_vekt_x = vekt_x/vekt_y
            k_vekt = vekt_x
        array = [[math.sqrt((((y-config.Y+1)*k_vekt_x)**2+((x-config.X+1)*k_vekt_y)**2)) for x in range(config.X_CONST)] for y in range(config.Y_CONST)]
        for y in range(config.Y_CONST):
            for x in range(config.X_CONST):
                if array[y][x] <= k_vekt:
                    recompileMap[y][x] = self.caveMap[y][x]
                else:
                    recompileMap[y][x] = ' '
