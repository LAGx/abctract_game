import phisic.figure.figure as figure
import pygame
import phisic.vector
import config
import game_objects.bullet.regular
from serving.cord import *

class Player():
    pos = [float(0), float(0)]

    mouse = [0,0]
    mousepress = [0,0,0]
    __speed = float(4)
    __drug = float(0.25)
    skin = figure.Rect(pos[0],pos[1],15,15)
    rBullet = game_objects.bullet.regular.RegularBullet()

    main_vec = phisic.vector.Vector()
    up_vec = phisic.vector.Vector()
    right_vec = phisic.vector.Vector()
    drug_vec = phisic.vector.Vector()

    def __init__(self):
        self.skin.color = config.Color.player
        self.up_vec.changeYEx(self.__speed)
        self.right_vec.changeXEx(self.__speed)
        self.aim = pygame.image.load("aim.png")
        self.aim.set_colorkey((0,0,0))
        pygame.mouse.set_pos((0,0))
        self.isInit = False

    def control(self):
        self.mouse = (pygame.mouse.get_pos()[0]-10, pygame.mouse.get_pos()[1]-10)

        self.mousepress = pygame.mouse.get_pressed()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.main_vec.changeXPlus(-self.right_vec.posX)
        if keys[pygame.K_d]:
            self.main_vec.changeXPlus(self.right_vec.posX)
        if keys[pygame.K_w]:
            self.main_vec.changeYPlus(self.up_vec.posY)
        if keys[pygame.K_s]:
            self.main_vec.changeYPlus(-self.up_vec.posY)

    def update(self, canvas):

        if self.mousepress[0]:
            self.rBullet.initBullet([ self.pos[0], self.pos[1] ], list(self.mouse))

        if True and self.rBullet.isInit:#while collider whith enother object
            self.rBullet.fire(canvas)

        self.control()
        canvas.blit(self.aim, self.mouse)
        self.drug_vec.changeXEx(self.main_vec.posX)
        self.drug_vec.changeYEx(self.main_vec.posY)
        self.drug_vec.multiply(self.__drug)
        self.drug_vec.invert()
        self.main_vec.plus(self.drug_vec)
        self.skin.move_by(self.main_vec.posX, self.main_vec.posY)
        self.pos[0] = self.skin.collision.x
        self.pos[1] = -self.skin.collision.y
        self.skin.draw(canvas)