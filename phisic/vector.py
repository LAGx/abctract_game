import numpy
import pygame


class Vector:

    def __init__(self, x = 0, y = 0):
        self.posX = float(x)
        self.posY = float(y)

    def getLenth(self):
         return numpy.sqrt((self.posX * self.posX) + (self.posY * self.posY))

    #Ex - заменить
    #Plus - добавить
    def changeXEx(self,X):
        self.posX = X
    def changeXPlus(self,X):
        self.posX = self.posX + X
    def changeYEx(self,Y):
        self.posY = -Y
    def changeYPlus(self,Y):
        self.posY = self.posY + Y

    def invert(self):
        self.posX = -self.posX
        self.posY = self.posY



    def multiply(self, coef):
        self.posX = coef * self.posX
        self.posY = coef * self.posY

    def plus(self, vec):
        self.posX = self.posX + vec.posX
        self.posY = self.posY + vec.posY

    def draw(self,canvas, cord, localX, localY,lenth, size = 2, color = (0, 255, 0)):
        pygame.draw.line(canvas, color, [cord.gloX(localX), cord.gloY(localY)], [self.posX*lenth+cord.gloX(localX), (-self.posY*lenth+cord.gloY(localY))], size)
        pygame.draw.circle(canvas, (255, 0,0), [int(self.posX*lenth+cord.gloX(localX)), int(-self.posY*lenth+cord.gloY(localY))], size)