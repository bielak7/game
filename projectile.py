import pygame
from CONST import *


class projectile(pygame.Rect):
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.h = 12
        self.w = 5
        self.type = str(type)

    def move(self):
        if self.type == "1":
            self.y -= PROJECTILE_SPEED
        else:
            self.y += PROJECTILE_SPEED



