__author__ = 'n7701-00-091'


numOfLevels = 10

## Cave size
fullLevelMap_X = 200
fullLevelMap_Y = 200

## Interface size
X = 14
Y = 10

Y_CONST = (Y * 2 - 1)
X_CONST = (X * 2 - 1)

## Icons
WALLS = {
"WALL_VERTICAL": "|",
"WALL_HORIZONTAL": "-",
"WALL_CROSS": "+"
}

OTHER_ICONS = {
"FREE_SPACE": "`",
"PLAYER": "@",
"ADDITIONAL_TIME": "H"
}

## Movement
UP = 72
DOWN = 80
LEFT = 75
RIGHT = 77

SPACE = 32
