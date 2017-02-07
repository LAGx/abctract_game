import pygame
import game_objects.body
import phisic.hitbox
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


body = game_objects.body.Rect([150, 150], [0,-3],6,50, "resource/lazer_sqr.png")
player = game_objects.body.Rect([200, 200], [-10,-10], 20, 20, "resource/aim.png")

player.speedCoef = 2
player.drugCoef = 0.1
player.delta_rotate = -2
body.delta_rotate = 1

while not gameExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        gameExit = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.vec.changeXPlus(-1)
    if keys[pygame.K_d]:
        player.vec.changeXPlus(1)
    if keys[pygame.K_w]:
        player.vec.changeYPlus(-1)
    if keys[pygame.K_s]:
        player.vec.changeYPlus(1)

    canvas.fill(config.Color.background)

    if phisic.collision.rect_rect(body.hitbox, player.hitbox):
        pygame.draw.circle(canvas, (200,60,60), [300, 200], 30)
    else:
        pygame.draw.circle(canvas, (20,55,20), [300, 200], 25)

    body.draw(canvas)
    body.visualDebag(canvas, (20, 200, 200))

    player.draw(canvas)
    player.visualDebag(canvas, (200,0,0))

    window.blit(canvas, (0, 0))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

#by K`VARK