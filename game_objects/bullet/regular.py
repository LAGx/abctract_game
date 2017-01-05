import phisic.vector
import pygame
import copy
from serving.cord import *

class RegularBullet:

    color = [153,0,0]
    speed = 40


    def __init__(self, start = None, end = None):

        start[0] += 10
        start[1] -= 10
        end[0] +=10
        end[1] +=10
        self.__vector = phisic.vector.Vector()
        self.__pos = start
        self.__vector.changeXEx(end[0] - start[0])
        self.__vector.changeYEx(end[1] + start[1])
        lenth = self.__vector.getLenth()
        self.__vector.changeXEx((self.__vector.posX)/lenth)
        self.__vector.changeYEx((-self.__vector.posY)/lenth)
        self.isInit = True

    def blit(self, canvas):
        pygame.draw.line(canvas, self.color, [self.__pos[0], -self.__pos[1]], [self.__pos[0]+self.__vector.posX*self.speed*3, -self.__pos[1]-self.__vector.posY*self.speed*3], 4)
        self.__pos[0] += self.__vector.posX * self.speed
        self.__pos[1] += self.__vector.posY * self.speed


