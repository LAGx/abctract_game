import phisic.vector
import pygame
from serving.cord import *

class RegularBullet:
    pos = [0, 0]
    vector = phisic.vector.Vector()
    color = [167,34,46]
    speed = 30
    isInit = False

    def __init__(self):
        pass

    def initBullet(self, start = [0,0], end = [0,0]):
        start[0] += 10
        start[1] -= 10
        end[0] +=10
        end[1] +=10
        self.pos = start
        self.vector.changeXEx(end[0] - self.pos[0])
        self.vector.changeYEx(end[1] + self.pos[1])
        lenth = self.vector.getLenth()
        self.vector.changeXEx((self.vector.posX)/lenth)
        self.vector.changeYEx((-self.vector.posY)/lenth)
        self.isInit = True

    def fire(self, canvas):
        pygame.draw.line(canvas,self.color, [self.pos[0], -self.pos[1]], [self.pos[0]+self.vector.posX*self.speed*3, -self.pos[1]-self.vector.posY*self.speed*3], 4)
        self.pos[0] += self.vector.posX * self.speed
        self.pos[1] += self.vector.posY * self.speed