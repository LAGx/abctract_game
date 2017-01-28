import pygame

import phisic.body
import graphicCore.window
from serving import write
from serving.cord import *
import phisic.collision

pygame.init()

write.clear()
window = graphicCore.window.createWindow()
canvas = pygame.Surface(config.currScreenSize())

pygame.key.set_repeat(1,1)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
gameExit = False
speed = 0.5
player = phisic.body.CircleBody([200, 250], 50)
body = phisic.body.RectBody([100, 200], 300, 200)

while not gameExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        gameExit = True
    if keys[pygame.K_a]:
        player.move([-speed, 0])
    if keys[pygame.K_d]:
        player.move([speed, 0])
    if keys[pygame.K_w]:
        player.move([0, -speed])
    if keys[pygame.K_s]:
        player.move([0, speed])

    canvas.fill(config.Color.background)
    player.draw(canvas, (200, 0, 0))
    if not phisic.collision.circle_rect(player, body):
        body.draw(canvas, (200, 0, 0))
    else:
        body.draw(canvas, (0, 200, 0))



    window.blit(canvas, (0, 0))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

#by K`VARK