import pygame

from serving.cord import *


class Figure:
    x_pos = 0.0
    y_pos = 0.0
    x_size = 0.0
    y_size = 0.0

    def __init__(self, x_pos, y_pos, x_size, y_size):
        self.collision = pygame.Rect(Global().gloX(x_pos), Global().gloY(y_pos), x_size, y_size)

class Rect(Figure):
    color = (255, 0, 0)

    def draw(self, canvas):
        pygame.draw.rect(canvas, self.color, self.collision)

    def move_by(self, by_x, by_y):
        self.collision.move_ip(by_x, by_y)
