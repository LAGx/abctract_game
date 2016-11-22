import pygame
import graphicCore.window
from coordinate.glob import *
import game_objects.player.player
import phisic.figure.figure as figure
import graphicCore.dialog.dialog
pygame.init()


#TODO: music class
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1, 13.0)

window = graphicCore.window.createWindow()
canvas = pygame.Surface(config.currScreenSize())
dialog = pygame.Surface((config.currDialogSize("x"),config.currDialogSize("y")))

alpha = 0

player = game_objects.player.player.Player()
house = figure.Rect(300, 250, 150, 250)
house.color = (15, 40, 40)
ruby = figure.Rect(-60, 80, 3, 3)
ruby.color = (255, 0, 127)
nubs = figure.Rect(-5, 5, 20, 20)
nubs.color = (80, 5, 5)

pygame.key.set_repeat(1,1)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
gameExit = False

look = graphicCore.dialog.dialog.Dialog(dialog)

while not gameExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            gameExit = True


    canvas.fill(config.Color.background)
    dialog.fill(config.Color.background_dialog)
####
    nubs.draw(canvas)
    house.draw(canvas)
    ruby.draw(canvas)
    player.update(canvas)
####
    dialog.set_alpha(alpha, 1)
    if player.skin.collision.colliderect(house.collision):
        if alpha < 120:
            alpha += 30
        look.showLine("It`s your house, master.")
    elif player.skin.collision.colliderect(ruby.collision):
        if alpha < 120:
            alpha += 30
        look.showLine("Ruby!!!!")
    elif player.skin.collision.colliderect(nubs.collision):
        if alpha < 120:
            alpha += 30
        look.showLine("W A S D - movement")
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
