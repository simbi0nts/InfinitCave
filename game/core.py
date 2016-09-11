import config
from random import *
import os
import math
from game.createLevel import CreateFirstLevel
from game.movementModul import MovementLogic
from game.enemyAI import EnemyMovement

#################################################################################
#                            Class gameCore                                     #
#################################################################################


class GameCore():

    def __init__(self):

        self.cave_map = [[config.OTHER_ICONS["FREE_SPACE"] for x in range(config.X_CONST)] for y in range(config.Y_CONST)]
        self.recompile_map = [[" " for x in range(config.X_CONST)] for y in range(config.Y_CONST)]
        self.passed_array = []
        self.start_position()
        self.move_points_done = 0
        self.move_points_left = 250
        self.moves_to_remove_one_light_point = 300
        self.light_points = 0
        self.health_points_max = 40
        self.health_points_now = 40
        self.message = ''
        self.flag = 1
        self.if_dymanic_light_option = 1
        self.deleted_symbol = config.OTHER_ICONS["FREE_SPACE"]
        self.void_array = [config.OTHER_ICONS["FREE_SPACE"] for x in range(config.X_CONST)]
        self.current_floor = 0
        self.new_levels = CreateFirstLevel()
        self.MovementLogic = MovementLogic()
        self.MovementLogic.cave_map = self.cave_map
        self.MovementLogic.current_floor = self.current_floor
        self.MovementLogic.new_levels = self.new_levels.level_map
        self.EnemyMovement = EnemyMovement()
        self.EnemyMovement.level_map = self.MovementLogic.new_levels
        self.EnemyMovement.put_enemies()
        self.EnemyMovement.new_levels = self.new_levels.level_map
        self.current_cave()

#####################################################################################

    def start_position(self):

        self.cave_map[config.Y_CONST // 2][config.X_CONST // 2] = config.OTHER_ICONS["PLAYER"]

#####################################################################################

    def move_point_incremental(self):

        if self.deleted_symbol == config.OTHER_ICONS["LEVEL_UP"] and self.flag == 1:
            self.MovementLogic.current_floor += 1
        if self.deleted_symbol == config.OTHER_ICONS["LEVEL_DOWN"] and self.flag == 1:
            self.MovementLogic.current_floor -= 1
        elif self.deleted_symbol == config.OTHER_ICONS["ADDITIONAL_TIME"]:
            self.move_points_left += 5
            if self.light_points - 3 > 0:
                self.light_points -= 3
            else:
                self.light_points = 0
            if self.health_points_now + 5 < self.health_points_max:
                self.health_points_now += 5
            else:
                self.health_points_now = self.health_points_max
        else:
            if self.move_points_left == 0:
                self.health_points_now -= 2
                self.message += 'YOU ARE STARVING! '
            else:
                self.move_points_left -= 1
            self.moves_to_remove_one_light_point -= 1
        if self.moves_to_remove_one_light_point == 0:
            if self.light_points != (min(config.X, config.Y)) - 2:
                self.light_points += 1
            if self.move_points_left == 0:
                self.moves_to_remove_one_light_point = randint(1, 3)
            else:
                self.moves_to_remove_one_light_point = randint(3, 6)
        if self.light_points == (min(config.X, config.Y)) - 2:
            if randint(0, 3) < 1:
                self.health_points_now -= 4
                self.message += 'SOMETHING IN THE DARK HURTS YOU! '
            else:
                self.health_points_now -= 2
                self.message += 'YOU ARE FREEZING! '
        self.move_points_done += 1

#####################################################################################

    def move(self, horizontal_move, vertical_move):

        self.message = ''
        if (self.cave_map[(config.Y_CONST // 2) + vertical_move][config.X_CONST // 2 + horizontal_move] not in config.WALLS.values()) \
                and (horizontal_move != 0 or vertical_move != 0):
            if self.deleted_symbol != config.OTHER_ICONS["LEVEL_DOWN"] or self.deleted_symbol != config.OTHER_ICONS["LEVEL_UP"]:
                self.new_levels.level_map[self.MovementLogic.current_floor][self.MovementLogic.Y + config.Y_CONST // 2][self.MovementLogic.X + config.X_CONST // 2] = \
                    config.OTHER_ICONS["FREE_SPACE"]
            if self.deleted_symbol == config.OTHER_ICONS["LEVEL_DOWN"]:
                self.new_levels.level_map[self.MovementLogic.current_floor][self.MovementLogic.Y + config.Y_CONST // 2][self.MovementLogic.X + config.X_CONST // 2] = \
                    config.OTHER_ICONS["LEVEL_UP"]
                self.flag = 1
            if self.deleted_symbol == config.OTHER_ICONS["LEVEL_UP"]:
                self.new_levels.level_map[self.MovementLogic.current_floor][self.MovementLogic.Y + config.Y_CONST // 2][self.MovementLogic.X + config.X_CONST // 2] = \
                    config.OTHER_ICONS["LEVEL_DOWN"]
                self.flag = 1
            self.deleted_symbol = self.cave_map[(config.Y_CONST // 2) + vertical_move][config.X_CONST // 2 + horizontal_move]
            if vertical_move != 0:
                if vertical_move == -1:
                    self.MovementLogic.move_up()
                elif vertical_move == 1:
                    self.MovementLogic.move_down()
            elif horizontal_move != 0:
                if horizontal_move == -1:
                    self.MovementLogic.move_left()
                if horizontal_move == 1:
                    self.MovementLogic.move_right()
            self.show_cave()
        if horizontal_move == 0 and vertical_move == 0:
            if self.deleted_symbol == config.OTHER_ICONS["LEVEL_DOWN"] or self.deleted_symbol == config.OTHER_ICONS["LEVEL_UP"]:
                self.flag = 0
            self.show_cave()

#####################################################################################

    def if_hurt_by_enemy(self):

        if self.cave_map[config.Y_CONST // 2][config.X_CONST // 2] == config.OTHER_ICONS["ENEMY"] or \
           self.cave_map[(config.Y_CONST // 2) - 1][config.X_CONST // 2] == config.OTHER_ICONS["ENEMY"] or \
           self.cave_map[(config.Y_CONST // 2) + 1][config.X_CONST // 2] == config.OTHER_ICONS["ENEMY"] or \
           self.cave_map[config.Y_CONST // 2][(config.X_CONST // 2) + 1] == config.OTHER_ICONS["ENEMY"] or \
           self.cave_map[config.Y_CONST // 2][(config.X_CONST // 2) - 1] == config.OTHER_ICONS["ENEMY"]:
            self.health_points_now -= 3
            self.message += 'OUCH!! HURTS!!'

#####################################################################################

    def current_cave(self):

        for y in range(config.Y_CONST):
            for x in range(config.X_CONST):
                self.cave_map[y][x] = self.MovementLogic.new_levels[self.MovementLogic.current_floor][self.MovementLogic.Y + y][self.MovementLogic.X + x]

#####################################################################################

    def show_cave(self):

        os.system('cls')
        self.EnemyMovement.enemy_check_direction()
        self.move_point_incremental()
        self.current_cave()
        self.if_hurt_by_enemy()
        self.start_position()
        self.recompile_level()
        print('\n')
        current_floor = '\tCurrent floor: ' + str(self.MovementLogic.current_floor)
        current_floor = self.beauty_space(current_floor)
        moves_done = '\tMoves done: %+4s' % str(self.move_points_done)
        moves_done = self.beauty_space(moves_done)
        moves_left = '\tMoves left: %+4s' % str(self.move_points_left)
        moves_left = self.beauty_space(moves_left)
        print(current_floor + '\n' + moves_done + '\n' + moves_left)
        health_bar = '{'
        for i in range(self.health_points_max):
            if i < self.health_points_now:
                health_bar += '/'
            else:
                health_bar += ' '
        health_bar += '}'
        health_bar = 'Health bar: ' + health_bar
        health_bar = self.beauty_space(health_bar)
        self.message = self.beauty_space(self.message)
        print(health_bar + '\n' + self.message)
        self.recompile_light_map(self.recompile_map, self.light_points)
        for y in range(config.Y_CONST):
            show_str_line = ''.join(self.recompile_map[y])
            print('\t\t' + show_str_line)

#####################################################################################

    def recompile_level(self):

        for y in range(config.Y_CONST):
            for x in range(config.X_CONST):
                code_id = 0
                if self.cave_map[y][x] in config.WALLS.values():
                    if y > 0:
                        if self.cave_map[y - 1][x] in config.WALLS.values():
                            code_id += 1
                    if x < config.X_CONST - 1:
                        if self.cave_map[y][x + 1] in config.WALLS.values():
                            code_id += 10
                    if y < config.Y_CONST - 1:
                        if self.cave_map[y + 1][x] in config.WALLS.values():
                            code_id += 100
                    if x > 0:
                        if self.cave_map[y][x - 1] in config.WALLS.values():
                            code_id += 1000
                    if code_id == 0:
                        self.cave_map[y][x] = config.WALLS["WALL_ALONE"]
                    elif code_id == 11:
                        self.cave_map[y][x] = config.WALLS["WALL_CORNER_UP_RIGHT"]
                    elif code_id == 101 or code_id == 1 or code_id == 100:
                        self.cave_map[y][x] = config.WALLS["WALL_VERTICAL"]
                    elif code_id == 110:
                        self.cave_map[y][x] = config.WALLS["WALL_CORNER_DOWN_RIGHT"]
                    elif code_id == 111:
                        self.cave_map[y][x] = config.WALLS["WALL_SIDE_LEFT"]
                    elif code_id == 1001:
                        self.cave_map[y][x] = config.WALLS["WALL_CORNER_UP_LEFT"]
                    elif code_id == 1010 or code_id == 10 or code_id == 1000:
                        self.cave_map[y][x] = config.WALLS["WALL_HORIZONTAL"]
                    elif code_id == 1100:
                        self.cave_map[y][x] = config.WALLS["WALL_CORNER_DOWN_LEFT"]
                    elif code_id == 1110:
                        self.cave_map[y][x] = config.WALLS["WALL_SIDE_DOWN"]
                    elif code_id == 1011:
                        self.cave_map[y][x] = config.WALLS["WALL_SIDE_UP"]
                    elif code_id == 1101:
                        self.cave_map[y][x] = config.WALLS["WALL_SIDE_RIGHT"]
                    elif code_id == 1111:
                        self.cave_map[y][x] = config.WALLS["WALL_CROSS"]

#####################################################################################

    def recompile_light_map(self, recompile_map, rad_light):

        vector_y = (config.Y - 1) - rad_light
        vector_x = (config.X - 1) - rad_light
        k_vector_x = 1
        k_vector_y = 1
        k_vector = vector_x
        if vector_x < vector_y:
            k_vector_y = vector_y / vector_x
            k_vector = vector_y
        elif vector_x > vector_y:
            k_vector_x = vector_x / vector_y
            k_vector = vector_x
        array = [[math.sqrt((((y - config.Y + 1) * k_vector_x) ** 2 + ((x - config.X + 1) * k_vector_y) ** 2)) for x in
                  range(config.X_CONST)] for y in range(config.Y_CONST)]
        for y in range(config.Y_CONST):
            for x in range(config.X_CONST):
                if array[y][x] <= k_vector:
                    recompile_map[y][x] = self.cave_map[y][x]
                else:
                    recompile_map[y][x] = ' '
        if self.if_dymanic_light_option:
            self.dynamic_light(recompile_map)

######################################################################################

    @staticmethod
    def dynamic_light(recompile_map):
        dynamic_light_array = [[[math.fabs(y - config.Y + 1), math.fabs(x - config.X + 1)] for x in range(config.X_CONST)] for y in range(config.Y_CONST)]
        for y in range(config.Y_CONST):
            for x in range(config.X_CONST):
                if x == 0 or y == 0 or x == config.X_CONST-1 or y == config.Y_CONST-1:
                    recompile_map[y][x] = ' '
        for y in range(config.Y_CONST):
            for x in range(config.X_CONST):
                if recompile_map[y][x] != ' ':
                    temp_array = []
                    main_y_arrays = y_array = dynamic_light_array[y][x][0]
                    main_x_arrays = x_array = dynamic_light_array[y][x][1]
                    len_of_main_vector = math.sqrt(x_array**2+y_array**2)
                    y_temp = y
                    x_temp = x
                    while x_array != -1 and y_array != -1:
                        if recompile_map[y_temp][x_temp] != ' ':
                            temp_array += [[y_temp, x_temp]]
                            len_of_1_part_of_2_vector = math.sqrt((x_array-1)**2+y_array**2)
                            len_of_2_part_of_2_vector = math.sqrt((main_x_arrays-x_array)**2+(main_y_arrays-y_array)**2)
                            len_of_1_part_of_1_vector = math.sqrt(x_array**2+(y_array-1)**2)
                            len_of_2_part_of_1_vector = math.sqrt((main_x_arrays-x_array)**2+(main_y_arrays-y_array)**2)
                            if math.fabs(len_of_main_vector-(len_of_1_part_of_1_vector+len_of_2_part_of_1_vector)) \
                                    < math.fabs(len_of_main_vector-(len_of_1_part_of_2_vector+len_of_2_part_of_2_vector)):
                                x_array -= 1
                                if x_temp < (config.X_CONST // 2):
                                    x_temp += 1
                                elif x_temp > (config.X_CONST // 2):
                                    x_temp -= 1
                            elif math.fabs(len_of_main_vector-(len_of_1_part_of_1_vector+len_of_2_part_of_1_vector)) \
                                    > math.fabs(len_of_main_vector-(len_of_1_part_of_2_vector+len_of_2_part_of_2_vector)):
                                y_array -= 1
                                if y_temp < (config.Y_CONST // 2):
                                    y_temp += 1
                                elif y_temp > (config.Y_CONST // 2):
                                    y_temp -= 1
                            elif math.fabs(len_of_main_vector-(len_of_1_part_of_1_vector+len_of_2_part_of_1_vector)) \
                                    == math.fabs(len_of_main_vector-(len_of_1_part_of_2_vector+len_of_2_part_of_2_vector)):
                                x_array -= 1
                                y_array -= 1
                                if x_temp < (config.X_CONST // 2):
                                    x_temp += 1
                                elif x_temp > (config.X_CONST // 2):
                                    x_temp -= 1
                                if y_temp < (config.Y_CONST // 2):
                                    y_temp += 1
                                elif y_temp > (config.Y_CONST // 2):
                                    y_temp -= 1
                            if recompile_map[y_temp][x_temp] in config.WALLS.values():
                                for i in range(len(temp_array)):
                                    i_y = temp_array[i][0]
                                    i_x = temp_array[i][1]
                                    if recompile_map[i_y][i_x] not in config.WALLS.values():
                                        recompile_map[i_y][i_x] = ' '
                        else:
                            for i in range(len(temp_array)):
                                    i_y = temp_array[i][0]
                                    i_x = temp_array[i][1]
                                    recompile_map[i_y][i_x] = ' '
                            break
        for y in range(config.Y_CONST - 1):
            for x in range(config.X_CONST - 1):
                if recompile_map[y][x] in config.WALLS.values() and \
                        (recompile_map[y + 1][x] not in config.OTHER_ICONS.values() and
                         recompile_map[y][x + 1] not in config.OTHER_ICONS.values() and
                         recompile_map[y - 1][x] not in config.OTHER_ICONS.values() and
                         recompile_map[y][x - 1] not in config.OTHER_ICONS.values()):
                    recompile_map[y][x] = ' '
                if recompile_map[y][x] != ' '  and \
                        (recompile_map[y + 1][x] == ' ' and
                         recompile_map[y][x + 1] == ' ' and
                         recompile_map[y - 1][x] == ' ' and
                         recompile_map[y][x - 1] == ' '):
                    recompile_map[y][x] = ' '
        if recompile_map[config.Y_CONST - 1][config.X_CONST // 2] in config.WALLS.values():
            recompile_map[config.Y_CONST - 1][config.X_CONST // 2] = ' '
        if recompile_map[config.Y_CONST // 2][config.X_CONST - 1] in config.WALLS.values():
            recompile_map[config.Y_CONST // 2][config.X_CONST - 1] = ' '
        if recompile_map[0][config.X_CONST // 2] in config.WALLS.values():
            recompile_map[0][config.X_CONST // 2] = ' '
        if recompile_map[config.Y_CONST // 2][0] in config.WALLS.values():
            recompile_map[config.Y_CONST // 2][0] = ' '

######################################################################################

    @staticmethod
    def beauty_space(return_string):

        space_string = '\t\t'
        for x in range(config.X - len(return_string) // 2):
            space_string += ' '
        return_string = space_string + return_string
        return return_string