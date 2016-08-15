__author__ = 'n7701-00-091'

import config

class CreateFirstLevel():

    def __init__(self):

        newLevel = [[' ' for y in range(config.fullLevelMap_Y)] for x in range(config.fullLevelMap_X)]
        levelMap = [newLevel for x in range(config.numOfLevels)]

    def firstLevel(self):
        tempNewLevel = self.newLevel
        
