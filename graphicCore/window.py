import config
import pygame


def createWindow():
    if config.screen_mode == "full":
        window = pygame.display.set_mode(config.currScreenSize(), pygame.FULLSCREEN, 32)
        pygame.display.set_caption('Fullscreen mode')
    else:
        window = pygame.display.set_mode(config.currScreenSize(), 0, 32)
        if  config.screen_mode == "normal":
            pygame.display.set_caption('Normal mode')
        elif config.screen_mode == "test":
            pygame.display.set_caption('Test mode')
        else:
            window = pygame.display.set_mode((1, 1))
            print("invalid launch_mode")


    return window

