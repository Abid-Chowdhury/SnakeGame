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
