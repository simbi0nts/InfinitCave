
import os, time
import config
from msvcrt import getch


#####################################################################################
###                            Class startGameScr                                 ###
#####################################################################################

class startGameScr():

    def __init__(self):
        self.textStartGame = [' ', ' ', ' ',
                              ' _______  ______    _______  _______  _______    _______  __    _  __   __    ___   _  _______  __   __ ',
                              '|       ||    _ |  |       ||       ||       |  |   _   ||  |  | ||  | |  |  |   | | ||       ||  | |  |',
                              '|    _  ||   | ||  |    ___||  _____||  _____|  |  |_|  ||   |_| ||  |_|  |  |   |_| ||    ___||  |_|  |',
                              '|   |_| ||   |_||_ |   |___ | |_____ | |_____   |       ||       ||       |  |      _||   |___ |       |',
                              '|    ___||    __  ||    ___||_____  ||_____  |  |       ||  _    ||_     _|  |     |_ |    ___||_     _|',
                              '|   |    |   |  | ||   |___  _____| | _____| |  |   _   || | |   |  |   |    |    _  ||   |___   |   |  ',
                              '|___|    |___|  |_||_______||_______||_______|  |__| |__||_|  |__|  |___|    |___| |_||_______|  |___|']

    def printStartMenu(self):
        for x in range(len(self.textStartGame)):
            print(self.textStartGame[x])


#####################################################################################
###                            Class endGame                                      ###
#####################################################################################

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