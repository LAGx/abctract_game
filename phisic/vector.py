import numpy
import pygame


class Vector:
    posX = 0.0
    posY = 0.0
    __lenth = 0.0

    def getLenth(self):
        self.__lenth = numpy.sqrt((self.posX * self.posX) + (self.posY * self.posY))
        return self.__lenth


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