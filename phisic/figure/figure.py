import pygame
from coordinate.glob import *

class figure:
    x_pos = 0.0
    y_pos = 0.0
    x_size = 0.0
    y_size = 0.0

    def __init__(self, x_pos, y_pos, x_size, y_size):
        self.collision = pygame.Rect(GlobalCord().gloX(x_pos), GlobalCord().gloY(y_pos), x_size, y_size)

class rect(figure):
    color = (255, 0, 0)

    def draw(self, canvas):
        pygame.draw.rect(canvas, self.color, self.collision)

    def move_by(self, by_x, by_y):
        self.collision.move_ip(by_x, by_y)

    def teleport(self, x, y):
        self.collision.move(x, y)