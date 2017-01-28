import phisic.body
import serving.write as log
import numpy

def point_rect(p, rect, warning=True):  # service function, better to use circle_rect, with circle.radius=0
    if warning:
        log.warning("don`t recommend to use point_rect.(use circle_rect, with circle.radius=0)")
    allSquare = 0

    for i in range(0, 3):
        allSquare += square(p, rect.point[i], rect.point[i+1])
    allSquare += square(p, rect.point[3], rect.point[0])

    return False if allSquare > rect.square else True


def point_circle(p, circle, warning=True):  # service function, better to use circle_circle, with circle.radius=0
    if warning:
        log.warning("don`t recommend to use point_circle.(use circle_circle, with circle.radius=0")
    return True if length(p, circle.point) <= circle.radius else False


def rect_rect(rect_1, rect_2):
    for i in range(0,4 ):
        if point_rect(rect_1.point[i], rect_2, False):
            return True

    for i in range(0,4 ):
        if point_rect(rect_2.point[i], rect_1, False):
            return True

    return False


def circle_rect(circle, rect):
    d1 = length(rect.point[0], rect.point[1])
    d2 = length(rect.point[1], rect.point[3])

    def d(xr, yr, x1,y1,x2,y2):     #length from point to line
        return abs(xr*(y2-y1)+yr*(x1-x2) -x1*y2 + y1*x2)/numpy.sqrt(pow(y2-y1,2)+pow(x1-x2,2))

    greenHor = d(circle.point.p[0], circle.point.p[1], rect.point[0].p[0], rect.point[0].p[1], rect.point[2].p[0], rect.point[2].p[1])
    greenVer = d(circle.point.p[0], circle.point.p[1], rect.point[2].p[0], rect.point[2].p[1], rect.point[3].p[0], rect.point[3].p[1])
    redHor   = d(circle.point.p[0], circle.point.p[1], rect.point[2].p[0], rect.point[2].p[1], rect.point[3].p[0], rect.point[3].p[1])
    redVer   = d(circle.point.p[0], circle.point.p[1], rect.point[0].p[0], rect.point[0].p[1], rect.point[1].p[0], rect.point[1].p[1])

    if (greenHor + redHor) <= d1 and (greenVer + redVer) <= d2:
        return True
    elif (greenVer + redVer) <= d2 and (greenHor <= circle.radius or redHor <= circle.radius):
        return True
    elif (greenHor + redHor) <= d1 and (greenVer <= circle.radius or redVer <= circle.radius):
        return True
    else:
        return False


def circle_circle(circle_1, circle_2):
    return True if length(circle_1.point, circle_2.point) <= circle_1.radius + circle_2.radius else False


def length(p_1, p_2):
    return numpy.sqrt(pow((p_1.p[0] - p_2.p[0]), 2) + pow((p_1.p[1] - p_2.p[1]), 2))


def square(a, b, c):
    return abs(0.5*((b.p[0]-a.p[0])*(c.p[1]-a.p[1])-(b.p[1]-a.p[1])*(c.p[0]-a.p[0])))
