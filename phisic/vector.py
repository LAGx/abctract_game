import numpy
import pygame
import serving.write as log
import math

class Vector:

    def __init__(self, x = 0, y = 0, point1 = None, point2 = None):
        if point1 == None and point2 == None:
            self.posX = float(x)
            self.posY = float(y)
        else:
            self.posX = point2.p[0] - point1.p[0]
            self.posY = point2.p[1] - point1.p[1]

    def getLenth(self):
         return numpy.sqrt((self.posX * self.posX) + (self.posY * self.posY))

    def getCordList(self):
        return [self.posX, self.posY]

    def normalize(self):
        lenth = self.getLenth()
        self.posX = self.posX/lenth
        self.posY = self.posY/lenth

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

    def multiplyAndGetCordList(self, coef):
        return [coef * self.posX, coef * self.posY]

    def isZero(self):
        return True if math.fabs(self.posX) < 0.00001 and math.fabs(self.posY) < 0.00001 else False
        


def getScalar(vec1, vec2): 
    scalar = (vec1.posX*vec2.posX + vec1.posY*vec2.posY)/(vec1.getLenth() * vec2.getLenth())
    return scalar