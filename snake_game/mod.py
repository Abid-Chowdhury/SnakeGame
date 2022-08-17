from label import Label
from pathlib import Path
import pygame as pg

# Defining path for the images
images_path = Path(__file__).parents[1] / "images"


def put_number_on_screen(i, number, score, surface, x,  y):
    zero_label = Label(pg.image.load(images_path / "zero_snake_img.png"), 4.1)
    one_label = Label(pg.image.load(images_path / "one_snake_img.png"), 4.1)
    two_label = Label(pg.image.load(images_path / "two_snake_img.png"), 4.1)
    three_label = Label(pg.image.load(images_path / "three_snake_img.png"), 4.1)
    four_label = Label(pg.image.load(images_path / "four_snake_img.png"), 4.1)
    five_label = Label(pg.image.load(images_path / "five_snake_img.png"), 4.1)
    six_label = Label(pg.image.load(images_path / "six_snake_img.png"), 4.1)
    seven_label = Label(pg.image.load(images_path / "seven_snake_img.png"), 4.1)
    eight_label = Label(pg.image.load(images_path / "eight_snake_img.png"), 4.1)
    nine_label = Label(pg.image.load(images_path / "nine_snake_img.png"), 4.1)

    if score < 100 and score > 9: 
        if i == 0: x -= 14
        else: x += 14
    elif score < 1000 and score > 99:
        if i == 0: x -= 28
        elif i == 2: x += 28

    if number == 1: one_label.draw(x, y, surface)
    elif number == 2: two_label.draw(x, y, surface)
    elif number == 3: three_label.draw(x, y, surface)
    elif number == 4: four_label.draw(x, y, surface)
    elif number == 5: five_label.draw(x, y, surface)
    elif number == 6: six_label.draw(x, y, surface)
    elif number == 7: seven_label.draw(x, y, surface)
    elif number == 8: eight_label.draw(x, y, surface)
    elif number == 9: nine_label.draw(x, y, surface) 
    elif number == 0: zero_label.draw(x, y, surface)
