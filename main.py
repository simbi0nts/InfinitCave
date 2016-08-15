from msvcrt import getch
from game.core import gameCore
import config, os
from game.initScreen import endGame

class MainClass():

    def __init__(self):
        self.selfRunning = True
        self.endGame = endGame()
        self.Core = gameCore()

    def startGame(self):

        while(self.selfRunning):

            keyPress = getch()

            if (ord(keyPress) == config.SPACE):
                self.Core.doMessUp()

            if (ord(keyPress) == config.UP):
                self.Core.move(0, -1)

            if (ord(keyPress) == config.DOWN):
                self.Core.move(0, 1)

            if (ord(keyPress) == config.RIGHT):
                self.Core.move(1, 0)

            if (ord(keyPress) == config.LEFT):
                self.Core.move(-1, 0)

            if (self.Core.caveMap[(config.Y_CONST//2)+1][config.X_CONST//2] in config.WALLS.values() and \
                self.Core.caveMap[(config.Y_CONST//2)-1][config.X_CONST//2] in config.WALLS.values() and \
                self.Core.caveMap[config.Y_CONST//2][(config.X_CONST//2)+1] in config.WALLS.values() and \
                self.Core.caveMap[config.Y_CONST//2][(config.X_CONST//2)-1] in config.WALLS.values()):
                    self.selfRunning = self.endGame.newGame("\n\n\t\t\t\t YOU ARE DEAD")
                    if self.selfRunning:
                        self.Core = gameCore()
                        os.system("cls")
                        print('\n\n\n\n\n\n\n\t\t\t\t PRESS ANY ARROW KEY')

            if (self.Core.movePointsLeft == 0):
                    self.selfRunning = self.endGame.newGame("\n\n\t\t\t\t YOU ARE STARVE")
                    if self.selfRunning:
                        self.Core = gameCore()
                        os.system("cls")
                        print('\n\n\n\n\n\n\n\t\t\t\t PRESS ANY ARROW KEY')

            if (self.Core.lightPoints == (max(config.X, config.Y)-1)):
                self.selfRunning = self.endGame.newGame("\n\n\t\t\t    YOU ARE OUT OF LIGHT")
                if self.selfRunning:
                    self.Core = gameCore()
                    os.system("cls")
                    print('\n\n\n\n\n\n\n\t\t\t\t PRESS ANY ARROW KEY')

if __name__=='__main__':
    mainCLS = MainClass()
    mainCLS.startGame()