import math
import serving.write as log
import pygame
import phisic.vector


class Point:
    def __init__(self, xy):
        self.p = [0,0]
        self.change(xy, "add")

    def change(self, pointB, mode):   #mode = "add", "instead"
        error = False
        if Point == type(pointB):
            if mode == "add":
                for i in range(0, 2):
                    self.p[i] += pointB.p[i]
            elif mode == "instead":
                for i in range(0, 2):
                    self.p[i] = pointB.p[i]
            else:
                error = True

        elif list == type(pointB):
            if mode == "add":
                for i in range(0, 2):
                    self.p[i] += pointB[i]
            elif mode == "instead":
                for i in range(0, 2):
                    self.p[i] = pointB[i]
            else:
                error = True

        else:
            log.error("bad object type in Point.change()", timing=False)
        if error:
            log.error("mode invalid in Point.change()", timing=False)


class Rect:
    # (x,y)  [1] ********* [2]     (lenth)
    #            *********
    # (width)[3] ********* [4]

    def __init__(self, listCords=[0, 0], lenth = 0, width = 1):   #width = 1 - line   (x,y)*********(lenth)
        self.point = [0,0,0,0]
        for i in range(0, 4):
            self.point[i] = Point(listCords)

        self.point[0].change([0, 0], "add")
        self.point[1].change([0,lenth], "add")
        self.point[2].change([width, 0], "add")
        self.point[3].change([width, lenth], "add")
        self.vec = phisic.vector.Vector(self.point[1].p[0] - self.point[0].p[0], self.point[1].p[1] - self.point[0].p[1])
        self.square = lenth * width

    def move(self, xy):
        for i in range(0, 4):
            self.point[i].change(xy, "add")

    def draw(self, canvas, color = (200,0,0)):
        for i in range(0, 4):
            pygame.draw.circle(canvas, color, [int(self.point[i].p[0]), int(self.point[i].p[1])], 2)

    def rotate(self, basePoint = Point([0, 0]), angle=0):
        for i in range(0, 4):
            self.point[i].change([-basePoint.p[0], -basePoint.p[1]],"add")
            self.point[i].change([self.point[i].p[0]*math.cos(angle) - self.point[i].p[1]*math.sin(angle), self.point[i].p[0]*math.sin(angle) + self.point[i].p[1]*math.cos(angle)],"instead")
            self.point[i].change(basePoint, "add")

    def getAndUpdateVector(self): # - line [0]*********[1]
        self.vec.changeXEx(self.point[1].p[0] - self.point[0].p[0])
        self.vec.changeYEx(self.point[1].point[1] - self.point[0].p[1])
        return self.vec

class Circle:

    def __init__(self, listCords, radius = 0): #0 - point body if you want collis point and point (circle r=0)
        import numpy
        self.point = Point(listCords)
        self.radius = radius

    def draw(self, canvas, color = (100,100,200)):
        pygame.draw.circle(canvas, color, (int(self.point.p[0]), int(self.point.p[1])), self.radius)

    def rotate(self, basePoint = Point([0, 0]), angle=0): #angle degeese
            self.point.change([-basePoint.p[0], -basePoint.p[1]],"add")
            self.point.change([self.point.p[0]*math.cos(angle) - self.point.p[1]*math.sin(angle), self.point.p[0]*math.sin(angle) + self.point.p[1]*math.cos(angle)],"instead")
            self.point.change(basePoint, "add")

    def move(self, xy):
        self.point.change(xy, "add")
        