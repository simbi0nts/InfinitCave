from msvcrt import getch
from game.core import GameCore
import config
import os
from game.initScreen import EndGame
from game.initScreen import StartGameScr


class MainClass():
    def __init__(self):

        self.self_running = True
        self.EndGame = EndGame()
        self.StartGameSrc = StartGameScr()
        self.Core = GameCore()

    def start_game(self):

        self.StartGameSrc.print_start_menu()

        key_press = getch()

        if ord(key_press):
            self.Core.show_cave()

        while self.self_running:

            key_press = getch()

            if ord(key_press) == config.SPACE:
                self.Core.move(0, 0)

            if ord(key_press) == config.UP:
                self.Core.move(0, -1)

            if ord(key_press) == config.DOWN:
                self.Core.move(0, 1)

            if ord(key_press) == config.RIGHT:
                self.Core.move(1, 0)

            if ord(key_press) == config.LEFT:
                self.Core.move(-1, 0)

            if (self.Core.cave_map[(config.Y_CONST // 2) + 1][config.X_CONST // 2] in config.WALLS.values() and
                self.Core.cave_map[(config.Y_CONST // 2) - 1][config.X_CONST // 2] in config.WALLS.values() and
                self.Core.cave_map[config.Y_CONST // 2][(config.X_CONST // 2) + 1] in config.WALLS.values() and
                    self.Core.cave_map[config.Y_CONST // 2][(config.X_CONST // 2) - 1] in config.WALLS.values()):
                self.self_running = self.EndGame.new_game("\n\n\t\t\t           YOU ARE DEAD")
                if self.self_running:
                    self.Core = GameCore()
                    os.system("cls")
                    self.StartGameSrc.print_start_menu()
                else:
                    break

            if self.Core.move_points_left == 0 and self.Core.health_points_now <= 0:
                self.self_running = self.EndGame.new_game("\n\n\t\t\t          YOU ARE STARVE")
                if self.self_running:
                    self.Core = GameCore()
                    os.system("cls")
                    self.StartGameSrc.print_start_menu()
                else:
                    break

            if self.Core.light_points == (min(config.X, config.Y)) - 2 and self.Core.health_points_now <= 0:
                self.self_running = self.EndGame.new_game("\n\n\t\t\t       YOU ARE OUT OF LIGHT")
                if self.self_running:
                    self.Core = GameCore()
                    os.system("cls")
                    self.StartGameSrc.print_start_menu()
                else:
                    break

            if self.Core.health_points_now <= 0:
                self.self_running = self.EndGame.new_game("\n\n\t\t\t     KILLED BY A FILTHY ENEMY")
                if self.self_running:
                    self.Core = GameCore()
                    os.system("cls")
                    self.StartGameSrc.print_start_menu()
                else:
                    break


if __name__ == '__main__':
    mainCLS = MainClass()
    mainCLS.start_game()