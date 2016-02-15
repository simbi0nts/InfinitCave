__author__ = 'n7701-00-091'

import os, time
import config
from msvcrt import getch

class startGame():
    pass

class endGame():

    def __init__(self):
        self.textGameOver = [' ',' ',' ',
                            '     _______  _______  __   __  _______    _______  __   __  _______  ______  ',
                            '    |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ',
                            '    |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ',
                            '    |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ',
                            '    |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |',
                            '    |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |',
                            '    |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|']

    def animation(self):
        for i in range(len(self.textGameOver)):
            os.system('cls')
            for x in range(len(self.textGameOver)):
                if x >= len(self.textGameOver)-i:
                    print(self.textGameOver[x])
            time.sleep(1/10)

    def newGame(self, text):
        self.animation()
        while True:
            print(text)
            print("\n\n\t\t\t      Wanna play again?(Y/N)")
            keyPress = getch()
            if (ord(keyPress) == 121):
                return True
            elif (ord(keyPress) == 110):
                return False
            else:
                os.system('cls')
                for x in range(len(self.textGameOver)-1): print(self.textGameOver[x+1])
                print("\n\n\t\t\t\t  Wrong answer")
