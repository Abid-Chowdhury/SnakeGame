from label import Label
from pathlib import Path
from random import randint
import pygame as pg


# Defining path for the images and text file
images_path = Path(__file__).parents[1] / "images"
snake_game_path = Path(__file__).parents[1] / "snake_game"
snake_game_path = str(snake_game_path) + '\HISCORE.txt'

# Initializing pygame
pg.init()

# Initializing constant variables
WIDTH, HEIGHT = 960, 630

YELLOW = (255, 255, 0)
RED = (255 ,61, 65)
BLACK = (31, 32, 34)
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)
PINK = (255, 182, 201)
LIGHTPINK = (255, 219, 233)

GRIDSIZE = 30  
GRIDHEIGHT = HEIGHT / GRIDSIZE
GRIDWIDTH = WIDTH / GRIDSIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

RIGHT_RELATIVE = 1
LEFT_RELATIVE = 2 
LISTOFKEYS = [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_w, pg.K_s, pg.K_a, pg.K_d]


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


class SnakeAI(object):

    def __init__(self, surface):
        self.surface = surface
        self.reset()

    def get_head_pos(self):
        return self.pos[0]

    def lose(self):
        self.reward -= 1
        pass

    def draw(self):
        yellow_square_img = pg.image.load(images_path / "yellow_square_img.png")
        yellow_square_label = Label(yellow_square_img, 1)
        [yellow_square_label.draw(p[0], p[1], self.surface) for p in self.pos]

    def onKeyboard(self, action):
        turning = [RIGHT, DOWN, LEFT, UP]
        idx = turning.index(self.dir)

        if action is RIGHT_RELATIVE:
            new_idx = (idx + 1) % 4
            self.dir = turning[new_idx]

        elif action is LEFT_RELATIVE:
            new_idx = (idx - 1) % 4
            self.dir = turning[new_idx]

    def ate(self):
        # Seeing if snake ate food
        if list(self.get_head_pos()) == list(self.food.get_food_pos()):
            self.score += 1
            self.reward += 1
            self.food.randomize_pos(self.score, self.pos)

    def move(self):
        # Get head position and set it to a list
        self.new_head_loc = list(self.get_head_pos())

        # Moving snake 30 pixels
        if self.dir == RIGHT: 
            self.new_head_loc[0] += 30
        elif self.dir == LEFT:
            self.new_head_loc[0] -= 30
        elif self.dir == UP:
            self.new_head_loc[1] -= 30
        elif self.dir == DOWN:
            self.new_head_loc[1] += 30
        
        # Moving snakes body
        self.pos.insert(0, self.new_head_loc)
        if len(self.pos) > self.score:
            self.pos.pop()
        
    def check_dead(self):
        # If snake head hits anywhere on body then lose
        if len(self.pos) > 4 and self.new_head_loc in self.pos[2:]:
            self.lose()
            
        # If snake hits wall then lose
        if self.pos[0][0] == -30:
            self.lose()
        elif self.pos[0][0] == 960:
            self.lose()
        elif self.pos[0][1] == 630:
            self.lose()
        elif self.pos[0][1] == 30:
            self.lose()
        
        if self.turns <= 0:
            self.lose()

    def reset(self):
        self.pos = [(300, 300)]
        self.dir = RIGHT
        self.score = 1
        self.turns = 500
        self.food.pos = (690, 300)

        with open(snake_game_path, 'r') as f:
            data = f.read()

        lines = data.splitlines()
        self.highscore = int(lines[0]) 

    def draw_grid(self):
        for y in range(0, int(GRIDWIDTH)):
            for x in range(0, int(GRIDHEIGHT)):
                square = pg.Rect(y*GRIDSIZE, x*GRIDSIZE, GRIDSIZE, GRIDSIZE)
                
                # Every other block on grid is a different color
                if (x + y) % 2 == 0:
                    pg.draw.rect(self.surface, LIGHTPINK, square)
                else:
                    pg.draw.rect(self.surface, PINK, square)


class Food(object):

    def __init__(self):
        self.pos = (690, 300)

    def get_food_pos(self):
        return self.pos

    # Randomizes the foods positions
    def randomize_pos(self, length, snake_pos):
        self.pos = randint(0, int(GRIDWIDTH-1)) * GRIDSIZE, randint(0, int(GRIDHEIGHT-1)) * GRIDSIZE
        self.test_pos(length, snake_pos)

    # Checks if the food is not spawning in snake
    def test_pos(self, length, snake_pos):
        for p in snake_pos:
            if list(self.pos) == list(p):
                self.randomize_pos(length)

    def draw_food(self, surface):
        red_square_img = pg.image.load(images_path / "red_square_img.png")
        red_square_label = Label(red_square_img, 1)
        red_square_label.draw(self.pos[0], self.pos[1], surface)
