# Import files from parent directory
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from label import Label
from pathlib import Path
from random import randint
import pygame as pg
from constants import *
from food import *
from snakeAI import *

# Defining path for the images and text file
images_path = Path(__file__).parents[1] / "images"
snake_game_path = Path(__file__).parents[1] / "snake_game"
snake_game_path = str(snake_game_path) + '\HISCORE.txt'

# Initializing pygame
pg.init()

class Agent(object):
    
        def __init__(self):
            self.action = RIGHT_RELATIVE

        def run(self):
            snake = SnakeAI()
            
            while True:
                # Moves based on the ai's action
                snake.onKeyboard(self.action)
                snake.move(snake.dir)

                # Checks if snake ate food
                snake.ate()

                # Checks if snake died
                snake.check_dead()
                
                # Drawing everything to screen
                snake.draw_grid()
                snake.draw()
                snake.food.draw_food(snake.surface)

