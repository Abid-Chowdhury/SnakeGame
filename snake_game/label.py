import pygame as pg

pg.init()


class Label():

    def __init__(self, img, size):
        width = img.get_width()
        height = img.get_height()
        self.img = pg.transform.scale(img, (int(width * size), int(height * size)))

    def draw(self, x, y, surface):
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        surface.blit(self.img, (self.rect.x, self.rect.y))
        