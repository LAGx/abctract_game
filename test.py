import pygame
import game_objects.body
import game_objects.player
import phisic.hitbox
import graphicCore.window
from serving import write
from serving.cord import *
import phisic.collision
import serving.write as log


pygame.init()

write.clear()
window = graphicCore.window.createWindow()
canvas = pygame.Surface(config.currScreenSize())

pygame.key.set_repeat(1,1)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
gameExit = False
speed = 0.5


body = game_objects.body.Circle([150, 150], [0,-3],12, "resource/lazer_sqr.png")
player = game_objects.player.Player("resource/player.png", "resource/aim.png")

field = phisic.hitbox.Rect([0,0],config.currScreenSize()[1],config.currScreenSize()[0]) 

player.body.speed = 1
player.body.drug = 0.1
body.delta_rotate = 1

while not gameExit:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        player.getEvent(event)

    if key[pygame.K_ESCAPE]:
        gameExit = True

    player.getKeys(key, pygame.mouse.get_pos(),pygame.mouse.get_pressed())


    canvas.fill(config.Color.background)



    body.draw(canvas)
    #body.visualDebag(canvas, (20, 200, 200))

    player.draw(canvas)
    #player.body.visualDebag(canvas, (200,0,0))


    i = 0
    while i < len(player.allBullets):
        if phisic.collision.circle_rect(body.hitbox, player.allBullets[i].body.hitbox):
            pygame.draw.circle(canvas, (200,60,60), [300, 200], 30)
        

        if not phisic.collision.rect_rect(player.allBullets[i].body.hitbox, field):
            player.allBullets.pop(i)
        i +=1

    window.blit(canvas, (0, 0))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

#by K`VARK