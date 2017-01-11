import pygame

import phisic.body
import graphicCore.window
from serving import write
from serving.cord import *

pygame.init()

write.clear()
window = graphicCore.window.createWindow()
canvas = pygame.Surface(config.currScreenSize())

pygame.key.set_repeat(1,1)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
gameExit = False
speed = 0.05
angle = 0
body = phisic.body.RectBody([0, 0], 100, 50)
circle = phisic.body.CircleBody([200, 150], 3)
deltaPoint = phisic.body.Point([0, 0])
rotateP = phisic.body.Point([200, 150])
body.rotate(rotateP)
angle = 0
while not gameExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        gameExit = True
    if keys[pygame.K_a]:
        deltaPoint.change([-speed,0], "add")
    if keys[pygame.K_d]:
        deltaPoint.change([speed, 0], "add")
    if keys[pygame.K_w]:
        deltaPoint.change([0,-speed], "add")
    if keys[pygame.K_s]:
        deltaPoint.change([0,speed], "add")
    if keys[pygame.K_e]:
        circle.rotate(rotateP, 0.05)
    if keys[pygame.K_q]:
        circle.rotate(rotateP, -0.05)

    canvas.fill(config.Color.background)

    circle.draw(canvas, (0, 255, 0))
    circle.move(deltaPoint)

    body.draw(canvas)

    window.blit(canvas, (0, 0))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

#by K`VARCK