
import config
from random import *
import os, math
from game.createLevel import CreateFirstLevel

#####################################################################################
###                            Class gameCore                                     ###
#####################################################################################

class gameCore():

    def __init__(self):

        self.caveMap = [[config.OTHER_ICONS["FREE_SPACE"] for x in range(config.X_CONST)] for y in range(config.Y_CONST)]
        self.recompileMap = [[" " for x in range(config.X_CONST)] for y in range(config.Y_CONST)]
        self.startPosition()
        self.movePointsDone = 0
        self.movePointsLeft = 450
        self.movesToRemoveOneLightPoint = 700
        self.lightPoints = 0
        self.healthPointsMax = 40
        self.healthPointsNow = 40
        self.message = ''
        self.deletedSymb = config.OTHER_ICONS["FREE_SPACE"]
        self.voidArray = [config.OTHER_ICONS["FREE_SPACE"] for x in range(config.X_CONST)]
        self.level = 0
        self.newLevels = CreateFirstLevel()
        self.X = (config.fullLevelMap_X - config.X_CONST)//2
        self.Y = (config.fullLevelMap_Y - config.Y_CONST)//2
        self.currentCave()




#####################################################################################
    def startPosition(self):
        self.caveMap[config.Y_CONST//2][config.X_CONST//2] = config.OTHER_ICONS["PLAYER"]



#####################################################################################
    def movePointIncremental(self):

        if self.deletedSymb == 'H':
            self.movePointsLeft += 5
            if self.lightPoints-3 > 0:
                self.lightPoints -= 3
            else:
                self.lightPoints = 0
            if self.healthPointsNow+5 < self.healthPointsMax:
                self.healthPointsNow += 5
            else:
                self.healthPointsNow = self.healthPointsMax
        else:
            if self.movePointsLeft == 0:
                self.healthPointsNow -= 2
                self.message += 'YOU ARE STARVING! '
            else:
                self.movePointsLeft -= 1
            self.movesToRemoveOneLightPoint -= 1
        if self.movesToRemoveOneLightPoint == 0:
            if (self.lightPoints != (min(config.X, config.Y))-2):
                self.lightPoints += 1
            if self.movePointsLeft == 0:
                self.movesToRemoveOneLightPoint = randint(1, 3)
            else:
                self.movesToRemoveOneLightPoint = randint(3, 6)
        if (self.lightPoints == (min(config.X, config.Y))-2):
            if randint(0, 3) < 1:
                self.healthPointsNow -= 4
                self.message += 'SOMETHING IN THE DARK HURTS YOU! '
            else:
                self.healthPointsNow -= 2
                self.message += 'YOU ARE FREEZING! '
        self.movePointsDone += 1



#####################################################################################
    def move(self, HorizontalMove, VerticalMove):

        self.message = ''
        if self.caveMap[(config.Y_CONST//2)+VerticalMove][config.X_CONST//2+HorizontalMove] not in config.WALLS.values():
            self.deletedSymb = self.caveMap[(config.Y_CONST//2)+VerticalMove][config.X_CONST//2+HorizontalMove]
            self.caveMap[config.Y_CONST//2][config.X_CONST//2] = config.OTHER_ICONS["FREE_SPACE"]
            if VerticalMove != 0:
                if VerticalMove == -1:
                    for y in range(config.Y_CONST-1):
                        self.caveMap[config.Y_CONST-y-1] = self.caveMap[config.Y_CONST-y-2]
                    self.Y -= 1
                    self.caveMap[0] = self.newLevels.levelMap[self.level][self.Y+1][self.X:self.X+config.X_CONST]
                    #self.caveMap[0] = [config.OTHER_ICONS["FREE_SPACE"] for x in range(config.X_CONST)]
                elif VerticalMove == 1:
                    for y in range(config.Y_CONST-1):
                        self.caveMap[y] = self.caveMap[y+1]
                    self.Y += 1
                    self.caveMap[config.Y_CONST-1] = self.newLevels.levelMap[self.level][self.Y+config.Y_CONST][self.X:self.X+config.X_CONST]
                    #self.caveMap[config.Y_CONST-1] = [config.OTHER_ICONS["FREE_SPACE"] for x in range(config.X_CONST)]
            elif HorizontalMove != 0:
                if HorizontalMove == -1:
                    self.X -= 1
                    for y in range(config.Y_CONST):
                        #self.caveMap[y] = self.newLevels.levelMap[self.level][self.Y+y][self.X:self.X+config.X_CONST]
                        self.caveMap[y] = self.caveMap[y][:-1]
                        self.caveMap[y].insert(0, self.newLevels.levelMap[self.level][self.Y+y][self.X])
                    #self.caveMap[y].insert(0, config.OTHER_ICONS["FREE_SPACE"])
                if HorizontalMove == 1:
                    self.X += 1
                    for y in range(config.Y_CONST):
                        self.caveMap[y] = self.caveMap[y][1:]
                        self.caveMap[y].append(self.newLevels.levelMap[self.level][self.Y+y][self.X+config.X_CONST])
                    #self.caveMap[y].append(config.OTHER_ICONS["FREE_SPACE"])
            self.movePointIncremental()
            self.showCave()



#####################################################################################
    def doMessUp(self):

        someRandomIncremental = randint(1,10)
        for i in range(someRandomIncremental):
            freeSpaceLeft = 0
            inc = 0
            for y in range(config.Y_CONST):
                freeSpaceLeft += self.caveMap[y].count(config.OTHER_ICONS["FREE_SPACE"]) + self.caveMap[y].count(config.OTHER_ICONS["ADDITIONAL_TIME"])
            findElement = randint(0, freeSpaceLeft)
            hChance = randint(0, 10)
            for y in range(config.Y_CONST):
                for x in range(config.X_CONST):
                    if self.caveMap[y][x] == config.OTHER_ICONS["FREE_SPACE"] or self.caveMap[y][x] == config.OTHER_ICONS["ADDITIONAL_TIME"]:
                        if inc != findElement:
                            inc += 1
                        else:
                            if hChance == 1:
                                self.caveMap[y][x] = config.OTHER_ICONS["ADDITIONAL_TIME"]
                            else:
                                self.caveMap[y][x] = config.WALLS["WALL_ALONE"]
                            inc += 1
                            continue
        self.startPosition()


    def currentCave(self):
        for y in range(config.Y_CONST):
            for x in range(config.X_CONST):
                self.caveMap[y][x] = self.newLevels.levelMap[self.level][self.Y+y][self.X+x]


#####################################################################################
    def showCave(self):

        os.system('cls')
        #self.currentCave()
        self.startPosition()
        #self.doMessUp()
        self.recompileLevel()
        print('\n')
        movesDone = '\tMoves done: ' + str(self.movePointsDone)
        movesDone = self.beautySpace(movesDone)
        movesLeft = '\tMoves left: ' + str(self.movePointsLeft)
        movesLeft = self.beautySpace(movesLeft)
        print(movesDone + '\n' + movesLeft)
        healthBar = '{'
        for i in range(self.healthPointsMax):
            if i < self.healthPointsNow:
                healthBar += '/'
            else:
                healthBar += ' '
        healthBar += '}'
        healthBar = 'Health bar: ' + healthBar
        healthBar = self.beautySpace(healthBar)
        self.message = self.beautySpace(self.message)
        print(healthBar + '\n' + self.message)
        self.recomLightMap(self.recompileMap, self.lightPoints)
        for y in range(config.Y_CONST):
            showStrLine = ''.join(self.recompileMap[y])
            print('\t\t' + showStrLine)



#####################################################################################
    def recompileLevel(self):

        for y in range(config.Y_CONST):
            for x in range(config.X_CONST):
                code_id = 0
                if self.caveMap[y][x] in config.WALLS.values():
                    if y > 0:
                        if self.caveMap[y-1][x] in config.WALLS.values():
                            code_id += 1
                    if x < config.X_CONST-1:
                        if self.caveMap[y][x+1] in config.WALLS.values():
                            code_id += 10
                    if y < config.Y_CONST-1:
                        if self.caveMap[y+1][x] in config.WALLS.values():
                            code_id += 100
                    if x > 0:
                        if self.caveMap[y][x-1] in config.WALLS.values():
                            code_id += 1000
                    if code_id == 0:
                        self.caveMap[y][x] = config.WALLS["WALL_ALONE"]
                    elif code_id == 11:
                        self.caveMap[y][x] = config.WALLS["WALL_CORNER_UP_RIGHT"]
                    elif code_id == 101 or code_id == 1 or code_id == 100:
                        self.caveMap[y][x] = config.WALLS["WALL_VERTICAL"]
                    elif code_id == 110:
                        self.caveMap[y][x] = config.WALLS["WALL_CORNER_DOWN_RIGHT"]
                    elif code_id == 111:
                        self.caveMap[y][x] = config.WALLS["WALL_SIDE_LEFT"]
                    elif code_id == 1001:
                        self.caveMap[y][x] = config.WALLS["WALL_CORNER_UP_LEFT"]
                    elif code_id == 1010 or code_id == 10 or code_id == 1000:
                        self.caveMap[y][x] = config.WALLS["WALL_HORIZONTAL"]
                    elif code_id == 1100:
                        self.caveMap[y][x] = config.WALLS["WALL_CORNER_DOWN_LEFT"]
                    elif code_id == 1110:
                        self.caveMap[y][x] = config.WALLS["WALL_SIDE_DOWN"]
                    elif code_id == 1011:
                        self.caveMap[y][x] = config.WALLS["WALL_SIDE_UP"]
                    elif code_id == 1101:
                        self.caveMap[y][x] = config.WALLS["WALL_SIDE_RIGHT"]
                    elif code_id == 1111:
                        self.caveMap[y][x] = config.WALLS["WALL_CROSS"]



#####################################################################################
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



#####################################################################################
    def beautySpace(self, returnString):
        spaceString = '\t\t'
        for x in range(config.X - len(returnString)//2):
            spaceString += ' '
        returnString = spaceString + returnString
        return returnString