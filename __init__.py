import pygame
import graphicCore.window
from coordinate.glob import *
import phisic.vector
pygame.init()
pygame.font.init()

window = graphicCore.window.createWindow()
canvas = pygame.Surface(config.currScreenSize())
dialog = pygame.Surface((config.currDialogSize("x"),config.currDialogSize("y")))

filter = GlobalCord()
speed = 0.4
x = 0
y = 0
drug = 0.04
alpha = 0

main_vec = phisic.vector.Vector()
up_vec = phisic.vector.Vector()
right_vec = phisic.vector.Vector()
drug_vec = phisic.vector.Vector()
up_vec.changeYEx(speed)
right_vec.changeXEx(speed)
player = pygame.Rect(filter.gloX(0), filter.gloY(0), 10, 10)
house = pygame.Rect(300, 250, 100, 150)
ruby = pygame.Rect(filter.gloX(0), filter.gloY(0), 3, 3)

pygame.key.set_repeat(1,1)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
gameExit = False

font = pygame.font.Font(None, 30)
your_house = font.render("It`s your house, master.", 1, (100, 255, 200))
your_ruby = font.render("Ruby!!!!", 1, (100, 255, 200))
textpos1 = your_house.get_rect()
textpos2 = your_ruby.get_rect()
textpos1.centerx = dialog.get_rect().centerx
textpos2.centerx = dialog.get_rect().centerx

while not gameExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            gameExit = True
        if keys[pygame.K_a]:
            main_vec.changeXPlus(-right_vec.posX)
        if keys[pygame.K_d]:
            main_vec.changeXPlus(right_vec.posX)
        if keys[pygame.K_w]:
            main_vec.changeYPlus(up_vec.posY)
        if keys[pygame.K_s]:
            main_vec.changeYPlus(-up_vec.posY)
        if keys[pygame.K_f]:
            x = 0
            y = 0
            main_vec.posX = 0
            main_vec.posY = 0



    drug_vec.changeXEx(main_vec.posX)
    drug_vec.changeYEx(main_vec.posY)

    drug_vec.multiply(drug)
    drug_vec.invert()
    main_vec.plus(drug_vec)
    player.move_ip(main_vec.posX, main_vec.posY)
    x += main_vec.posX
    y += main_vec.posY

    canvas.fill(config.background)
    dialog.fill((10, 30,30))
####
    pygame.draw.rect(canvas, (5,30,30), house)
    player.move_ip(main_vec.posX, main_vec.posY)
    pygame.draw.rect(canvas, config.lights_1, player)
    pygame.draw.rect(canvas,config.lights_2, ruby)
####
    dialog.set_alpha(alpha, 1)
    if player.colliderect(house):
        if alpha < 120:
            alpha += 30
        dialog.blit(your_house, (textpos1[0], textpos1[1] + config.currDialogSize("y")/5))
    elif player.colliderect(ruby):
        if alpha < 120:
            alpha += 30
        dialog.blit(your_ruby, (textpos2[0], textpos2[1] + config.currDialogSize("y") / 5))
    else:
        if(alpha >= 0):
            alpha -= 30

    window.blit(canvas, (0, 0))
    window.blit(dialog, (0,config.currScreenSize()[1]-config.currDialogSize("y")))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

#by K`VARCK
