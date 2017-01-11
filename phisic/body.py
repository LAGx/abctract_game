import math
import serving.write as log
import pygame
import phisic.vector

class Point:
    def __init__(self, xy):
        self.point = [0,0]
        self.change(xy, "add")

    def change(self, pointB, mode):   #"add", "instead"
        error = False
        if Point == type(pointB):
            if mode == "add":
                for i in range(0, 2):
                    self.point[i] += pointB.point[i]
            elif mode == "instead":
                for i in range(0, 2):
                    self.point[i] = pointB.point[i]
            else:
                error = True

        elif list == type(pointB):
            if mode == "add":
                for i in range(0, 2):
                    self.point[i] += pointB[i]
            elif mode == "instead":
                for i in range(0, 2):
                    self.point[i] = pointB[i]
            else:
                error = True

        else:
            log.error("bad object type in Point.change()", timing=False)
        if error:
            log.error("mode invalid in Point.change()", timing=False)

class RectBody:
    # (x,y)  [1] ********* [2]     (lenth)
    #            *********
    # (width)[3] ********* [4]

    def __init__(self, listCords=[0, 0], lenth=0, width = 0):   #whidth = 0 - line   (x,y)*********(lenth)
        self.point = [0,0,0,0]
        for i in range(0, 4):
            self.point[i] = Point(listCords)

        self.point[0].change([0, 0], "add")
        self.point[1].change([0,lenth], "add")
        self.point[2].change([width, 0], "add")
        self.point[3].change([width, lenth], "add")
        self.vec = phisic.vector.Vector(self.point[1].point[0] - self.point[0].point[0], self.point[1].point[1] - self.point[0].point[1])

    def move(self, xy):
        for i in range(0, 4):
            self.point[i].change(xy, "add")

    def draw(self, canvas, color = (200,0,0)):
        for i in range(0, 4):
            pygame.draw.circle(canvas, color, [int(self.point[i].point[0]), int(self.point[i].point[1])], 2)

    def rotate(self, basePoint = Point([0, 0]), angle=0): #angle degeese
        for i in range(0, 4):
            self.point[i].change([-basePoint.point[0], -basePoint.point[1]],"add")
            self.point[i].change([self.point[i].point[0]*math.cos(angle) - self.point[i].point[1]*math.sin(angle), self.point[i].point[0]*math.sin(angle) + self.point[i].point[1]*math.cos(angle)],"instead")
            self.point[i].change(basePoint, "add")

    def getAndUpdateVector(self): # - line [0]*********[1]
        self.vec.changeXEx(self.point[1].point[0] - self.point[0].point[0])
        self.vec.changeYEx(self.point[1].point[1] - self.point[0].point[1])
        return self.vec

class CircleBody:

    def __init__(self, listCords, radius):
        self.point = Point(listCords)
        self.radius = radius

    def draw(self, canvas, color = (100,100,200)):
        pygame.draw.circle(canvas, color, (int(self.point.point[0]), int(self.point.point[1])), self.radius)

    def rotate(self, basePoint = Point([0, 0]), angle=0): #angle degeese
            self.point.change([-basePoint.point[0], -basePoint.point[1]],"add")
            self.point.change([self.point.point[0]*math.cos(angle) - self.point.point[1]*math.sin(angle), self.point.point[0]*math.sin(angle) + self.point.point[1]*math.cos(angle)],"instead")
            self.point.change(basePoint, "add")

    def move(self, xy):
        self.point.change(xy, "add")
        