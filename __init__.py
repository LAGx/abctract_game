import pygame

import game_objects.player.player
import graphicCore.window
import write
from serving.cord import *

pygame.init()

write.clear()
window = graphicCore.window.createWindow()
canvas = pygame.Surface(config.currScreenSize())
indicators = pygame.Surface((config.currIndicatorSize("x"),config.currIndicatorSize("y")))
write.log("oh, god...")
write.log("Time???", timing=True)
write.error("hmmm error?")
write.error("and whith time", timing=True)

alpha = 150
player = game_objects.player.player.Player()

pygame.key.set_repeat(1,1)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
gameExit = False

while not gameExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        gameExit = True


    canvas.fill(config.Color.background)
    indicators.fill(config.Color.background_dialog)
####
    player.update(canvas)
####
    indicators.set_alpha(alpha, 1)

    window.blit(canvas, (0, 0))
    window.blit(indicators, (0,0))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

#by K`VARCK
