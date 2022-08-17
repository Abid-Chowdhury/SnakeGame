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