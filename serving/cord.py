import config

class Global: #filter coord
    __native_cord = [0.0, 0.0]

    def __init__(self):
        self.__native_cord[0] = config.currScreenSize()[0]
        self.__native_cord[1] = config.currScreenSize()[1]

    def gloCord(self, x, y):
        return [self.__native_cord[0] / 2 + x, -y + (self.__native_cord[1] / 2)]

    def gloX(self, x):
        return self.__native_cord[0] / 2 + x

    def gloY(self, y):
        return -y + self.__native_cord[1] / 2