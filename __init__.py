import pygame
import game_objects.body
import game_objects.player
import phisic.hitbox
import graphicCore.window
import phisic.collision
import serving.write as log
import config

pygame.init()

log.clear()
window = graphicCore.window.createWindow()
canvas = pygame.Surface(config.currScreenSize())

pygame.key.set_repeat(1,1)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
gameExit = False


player = game_objects.player.Player("resource/player.png", "resource/aim.png")
player.body.speed = 1
player.body.drug = 0.1


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
    player.draw(canvas)
   
    window.blit(canvas, (0, 0))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

#by K`VARK