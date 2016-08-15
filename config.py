
numOfLevels = 3

## Cave size
fullLevelMap_X = 200
fullLevelMap_Y = 200

## Interface size
X = 30
Y = 12

Y_CONST = (Y * 2 - 1)
X_CONST = (X * 2 - 1)

## Icons
'''  ## OLD_WALLS
WALLS = {
"WALL_VERTICAL": "│",
"WALL_HORIZONTAL": "─",
"WALL_CORNER_UP_LEFT": "┘",
"WALL_CORNER_UP_RIGHT": "└",
"WALL_CORNER_DOWN_LEFT": "┐",
"WALL_CORNER_DOWN_RIGHT": "┌",
"WALL_SIDE_LEFT": "├",
"WALL_SIDE_RIGHT": "┤",
"WALL_SIDE_UP": "┴",
"WALL_SIDE_DOWN": "┬",
"WALL_CROSS": "┼"
}
'''

WALLS = {
"WALL_ALONE": "¤",
"WALL_VERTICAL": "║",
"WALL_HORIZONTAL": "═",
"WALL_CORNER_UP_LEFT": "╝",
"WALL_CORNER_UP_RIGHT": "╚",
"WALL_CORNER_DOWN_LEFT": "╗",
"WALL_CORNER_DOWN_RIGHT": "╔",
"WALL_SIDE_LEFT": "╠",
"WALL_SIDE_RIGHT": "╣",
"WALL_SIDE_UP": "╩",
"WALL_SIDE_DOWN": "╦",
"WALL_CROSS": "╬"
}


OTHER_ICONS = {
"FREE_SPACE": "`",
"PLAYER": "@",
"LEVEL_UP": "^",
"LEVEL_DOWN": "V",
"ADDITIONAL_TIME": "H"
}

## ⃝∩⌐⌂

## Movement
UP = 72
DOWN = 80
LEFT = 75
RIGHT = 77

SPACE = 32
