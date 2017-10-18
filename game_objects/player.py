import pygame
import phisic.hitbox
import phisic.collision
import game_objects.bullet
import game_objects.body
import config

class Player:

    #sqare 20x20
    def __init__(self, image, aim):
        self.body = game_objects.body.Rect([250,250], [-10, -10],20,20,image)
        #mouse block
        self.aim = game_objects.body.Rect([250,100], [-10, -10],20,20,aim)
        self.field = phisic.hitbox.Rect([0,0],config.currScreenSize()[1],config.currScreenSize()[0]) 
        self.mouse = [0,0]
        pygame.mouse.set_pos(([250,100]))
        self.mousepress = [0,0,0]
        self.allBullets = []
        self.aim.delta_rotate = 4
        self.body.speed = 1
        self.body.drug = 0.5
        self.fireDelay = 150
        self.lastTime = pygame.time.get_ticks()


    def getEvent(self, event):
        self.event = event
    def getKeys(self, key, mouse_pos, mouse_press):
        self.key = key
        self.mouse = mouse_pos
        self.mousepress = mouse_press

    def control(self):
        if self.key[pygame.K_a]:
            if self.body.hitboxStart.center.p[0] < 0:
                self.body.vec.posX = 0
            else:
                self.body.vec.changeXPlus(-1)
        if self.key[pygame.K_d]:
            if self.body.hitboxStart.center.p[0] > config.currScreenSize()[0]:
                self.body.vec.posX = 0
            else:
                self.body.vec.changeXPlus(1)
        if self.key[pygame.K_w]:
            if self.body.hitboxStart.center.p[1] < 0:
                self.body.vec.posY = 0
            else:
                self.body.vec.changeYPlus(-1)
        if self.key[pygame.K_s]:
            if self.body.hitboxStart.center.p[1] > config.currScreenSize()[1]:
                self.body.vec.posY = 0
            else:
                self.body.vec.changeYPlus(1)



    def fireRegular(self, canvas):
        
        if self.mousepress[0]:
            last = pygame.time.get_ticks()
            if self.fireDelay < last - self.lastTime:
                    lazer = game_objects.bullet.Lazer(self.body.hitboxStart.center.p,self.aim.hitboxStart.center, 20)
                    self.allBullets.append(lazer)
                    self.lastTime = pygame.time.get_ticks()
       
        i = 0
        while i < len(self.allBullets):
            if not phisic.collision.rect_rect(self.allBullets[i].body.hitbox, self.field):
                self.allBullets.pop(i)
            i +=1

        for bullet in self.allBullets:
            bullet.draw(canvas)
            


    def draw(self, canvas):

        self.control()
        self.fireRegular(canvas)
        self.body.rotateToPointFirst(self.aim.hitboxStart.center)
        self.aim.teleport(list(self.mouse))
        self.aim.draw(canvas)
        self.body.draw(canvas)
