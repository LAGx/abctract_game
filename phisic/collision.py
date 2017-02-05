import phisic.hitbox
import serving.write as log
import numpy

def point_rect(p, rect, warning=True):  # service function, better to use circle_rect, with circle.radius=0
    if warning:
        log.warning("don`t recommend to use point_rect.(use circle_rect, with circle.radius=0)")
    allSquare = 0

    for i in range(0, 3):
        allSquare += serviсeFunc.square(p, rect.point[i], rect.point[i+1])
    allSquare += serviсeFunc.square(p, rect.point[3], rect.point[0])

    return False if allSquare > rect.square else True


def point_circle(p, circle, warning=True):  # service function, better to use circle_circle, with circle.radius=0
    if warning:
        log.warning("don`t recommend to use point_circle.(use circle_circle, with circle.radius=0")
    return True if serviсeFunc.lengthPoint_point(p, circle.point) <= circle.radius else False


def rect_rect(rect_1, rect_2):
    for i in range(0,4 ):
        if point_rect(rect_1.point[i], rect_2, False):
            return True

    for i in range(0,4 ):
        if point_rect(rect_2.point[i], rect_1, False):
            return True

    return False


def circle_rect(circle, rect):

    if point_rect(circle.point, rect, False): #is inside circle.center
        return True

    l_0to1 = serviсeFunc.lengthPoint_point(rect.point[0], rect.point[1])+1 # (+1) becouse of inaccuracy of calculate
    l_0to2 = serviсeFunc.lengthPoint_point(rect.point[0], rect.point[2])+1

    d02 = serviсeFunc.lengthPoint_line(circle.point.p[0], circle.point.p[1],  rect.point[0].p[0], rect.point[0].p[1], rect.point[2].p[0], rect.point[2].p[1])
    d13 = serviсeFunc.lengthPoint_line(circle.point.p[0], circle.point.p[1],  rect.point[1].p[0], rect.point[1].p[1], rect.point[3].p[0], rect.point[3].p[1])
    d01 = serviсeFunc.lengthPoint_line(circle.point.p[0], circle.point.p[1],  rect.point[0].p[0], rect.point[0].p[1], rect.point[1].p[0], rect.point[1].p[1])
    d23 = serviсeFunc.lengthPoint_line(circle.point.p[0], circle.point.p[1],  rect.point[2].p[0], rect.point[2].p[1], rect.point[3].p[0], rect.point[3].p[1])
    
    #is collide circle whith sides of rect
    if d02 + d13 <= l_0to1:
        if d23 <= circle.radius or d01 <= circle.radius:
            return True
    if d01 + d23 <= l_0to2:
        if d02 <= circle.radius or d13 <= circle.radius:
            return True

    #is rect points in circle
    for i in range(0,4 ):
        if point_circle(rect.point[i], circle, False):
            return True

    return False

def circle_circle(circle_1, circle_2):
    return True if serviсeFunc.lengthPoint_point(circle_1.point, circle_2.point) <= circle_1.radius + circle_2.radius else False


class serviсeFunc:

    def lengthPoint_point(p_1, p_2):
       return numpy.sqrt(pow((p_1.p[0] - p_2.p[0]), 2) + pow((p_1.p[1] - p_2.p[1]), 2))

    def square(a, b, c):
      return abs(0.5*((b.p[0]-a.p[0])*(c.p[1]-a.p[1])-(b.p[1]-a.p[1])*(c.p[0]-a.p[0])))

    def lengthPoint_line(xr, yr, x1,y1,x2,y2):     #length from point(xr,yr) to line((x1,y1),(x2,y2))
      return abs(xr*(y2-y1)+yr*(x1-x2) -x1*y2 + y1*x2)/numpy.sqrt(pow(y2-y1,2)+pow(x1-x2,2))