import phisic.figure.figure as figure
import pygame
import phisic.vector
import config

class Player():
    pos_x = 0.0
    pos_y = 0.0
    __speed = 0.3
    __drug = 0.05
    skin = figure.Rect(pos_x,pos_y,10,10)

    main_vec = phisic.vector.Vector()
    up_vec = phisic.vector.Vector()
    right_vec = phisic.vector.Vector()
    drug_vec = phisic.vector.Vector()

    def __init__(self):
        self.skin.color = config.Color.player
        self.up_vec.changeYEx(self.__speed)
        self.right_vec.changeXEx(self.__speed)

    def control(self):
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.main_vec.changeXPlus(-self.right_vec.posX)
            if keys[pygame.K_d]:
                self.main_vec.changeXPlus(self.right_vec.posX)
            if keys[pygame.K_w]:
                self.main_vec.changeYPlus(self.up_vec.posY)
            if keys[pygame.K_s]:
                self.main_vec.changeYPlus(-self.up_vec.posY)
            if keys[pygame.K_f]:
                self.skin.teleport(0, 0)
                self.main_vec.posX = 0
                self.main_vec.posY = 0

    def update(self, canvas):
        self.control()
        self.drug_vec.changeXEx(self.main_vec.posX)
        self.drug_vec.changeYEx(self.main_vec.posY)
        self.drug_vec.multiply(self.__drug)
        self.drug_vec.invert()
        self.main_vec.plus(self.drug_vec)
        self.skin.move_by(self.main_vec.posX, self.main_vec.posY)
        self.skin.draw(canvas)