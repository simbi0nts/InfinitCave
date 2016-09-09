import os
import time
from msvcrt import getch


#################################################################################
#                            Class startGameScr                                 #
#################################################################################

class StartGameScr():
    def __init__(self):
        self.text_start_game = [' ', ' ', ' ',
                                ' _______  ______    _______  _______  _______    _______  __    _  __   __    ___   _  _______  __   __ ',
                                '|       ||    _ |  |       ||       ||       |  |   _   ||  |  | ||  | |  |  |   | | ||       ||  | |  |',
                                '|    _  ||   | ||  |    ___||  _____||  _____|  |  |_|  ||   |_| ||  |_|  |  |   |_| ||    ___||  |_|  |',
                                '|   |_| ||   |_||_ |   |___ | |_____ | |_____   |       ||       ||       |  |      _||   |___ |       |',
                                '|    ___||    __  ||    ___||_____  ||_____  |  |       ||  _    ||_     _|  |     |_ |    ___||_     _|',
                                '|   |    |   |  | ||   |___  _____| | _____| |  |   _   || | |   |  |   |    |    _  ||   |___   |   |  ',
                                '|___|    |___|  |_||_______||_______||_______|  |__| |__||_|  |__|  |___|    |___| |_||_______|  |___|']

    def print_start_menu(self):
        for x in range(len(self.text_start_game)):
            print(self.text_start_game[x])


#################################################################################
#                            Class endGame                                      #
#################################################################################

class EndGame():
    def __init__(self):
        self.text_game_over = [' ', ' ', ' ',
                               '     _______  _______  __   __  _______    _______  __   __  _______  ______  ',
                               '    |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ',
                               '    |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ',
                               '    |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ',
                               '    |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |',
                               '    |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |',
                               '    |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|']

    def animation(self):
        for i in range(len(self.text_game_over)):
            os.system('cls')
            for x in range(len(self.text_game_over)):
                if x >= len(self.text_game_over) - i:
                    print(self.text_game_over[x])
            time.sleep(1 / 10)

    def new_game(self, text):
        self.animation()
        while True:
            print(text)
            print("\n\n\t\t\t      Wanna play again?(Y/N)")
            key_press = getch()
            if ord(key_press) == 121:
                return True
            elif ord(key_press) == 110:
                return False
            else:
                os.system('cls')
                for x in range(len(self.text_game_over) - 1):
                    print(self.text_game_over[x + 1])
                print("\n\n\t\t\t\t  Wrong answer")