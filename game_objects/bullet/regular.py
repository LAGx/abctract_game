import phisic.vector
import pygame
from serving.cord import *

class RegularBullet:
    pos = [0, 0]
    vector = phisic.vector.Vector()
    color = [167,34,46]
    speed = 0.05
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
        print("x1: ", self.vector.posX, "y1: ", self.vector.posY)
        #self.vector.changeXEx((self.vector.posX)/self.vector.getLenth())
        #self.vector.changeYEx((-self.vector.posY) / self.vector.getLenth())
        print(self.vector.getLenth(), "x: ", self.vector.posX, "y: ", self.vector.posY)
        self.isInit = True

    def fire(self, canvas):
        pygame.draw.line(canvas,self.color, [self.pos[0], -self.pos[1]], [self.pos[0]+self.vector.posX*self.speed*5, -self.pos[1]-self.vector.posY*self.speed*5], 8)
        self.pos[0] += self.vector.posX * self.speed
        self.pos[1] += self.vector.posY * self.speed