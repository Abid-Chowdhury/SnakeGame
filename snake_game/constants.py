import pygame as pg

# Window size
WIDTH, HEIGHT = 960, 630

# Colors
YELLOW = (255, 255, 0)
LIGHTBLUE = (164, 219, 232)
BLUE = (137, 207, 240)
RED = (255 ,61, 65)
BLACK = (31, 32, 34)
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)

# Grid size
GRIDSIZE = 30  
GRIDHEIGHT = HEIGHT / GRIDSIZE
GRIDWIDTH = WIDTH / GRIDSIZE

# Direction
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

RIGHT_RELATIVE = 1
LEFT_RELATIVE = 2 
LIST_OF_KEYS = [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_w, pg.K_s, pg.K_a, pg.K_d]