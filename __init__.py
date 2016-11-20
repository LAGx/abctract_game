import pygame
import graphicCore.window
from coordinate.glob import *
import phisic.vector

pygame.init()

window = graphicCore.window.createWindow()
canvas = pygame.Surface(config.currScreenSize())

filter = GlobalCord()
speed = 0.4
x = 0
y = 0
drug = 0.04

main_vec = phisic.vector.Vector()
up_vec = phisic.vector.Vector()
right_vec = phisic.vector.Vector()
drug_vec = phisic.vector.Vector()
up_vec.changeYEx(speed)
right_vec.changeXEx(speed)


pygame.key.set_repeat(1,1)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
gameExit = False

while not gameExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameExit = True
            if event.key == pygame.K_a:
                main_vec.changeXPlus(-right_vec.posX)
            if event.key == pygame.K_d:
                main_vec.changeXPlus(right_vec.posX)
            if event.key == pygame.K_w:
                main_vec.changeYPlus(-up_vec.posY)
            if event.key == pygame.K_s:
                main_vec.changeYPlus(up_vec.posY)
            if event.key == pygame.K_f:
                x = 0
                y = 0
                main_vec.posX = 0
                main_vec.posY = 0

    drug_vec.changeXEx(main_vec.posX)
    drug_vec.changeYEx(main_vec.posY)

    drug_vec.multiply(drug)
    drug_vec.invert()
    main_vec.plus(drug_vec)

    x += main_vec.posX
    y += main_vec.posY
    print("X: ", drug_vec.posX, "            Y: ", drug_vec.posY)

    canvas.fill(config.background)
####
    pygame.draw.rect(canvas, config.lights_1, [int(filter.gloX(x-5)), int(filter.gloY(y+5)), 10, 10])
    pygame.draw.circle(canvas,config.lights_2, [int(filter.gloX(0)), int(filter.gloY(0))], 2)
    main_vec.draw(canvas, filter, x, y, 10)
####
    window.blit(canvas, (0, 0))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

#by K`VARCK
