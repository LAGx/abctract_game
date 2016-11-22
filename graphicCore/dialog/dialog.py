import pygame
import config

class Dialog:


    def __init__(self, dialog):
        pygame.font.init()
        self.font = pygame.font.Font(None, 30)
        self.canvas = dialog

    def showLine(self, text = "error: no text"):
        textLine = self.font.render(text, 1, config.Color.text_dialog)
        textpos = textLine.get_rect()
        textpos.centerx = self.canvas.get_rect().centerx
        self.canvas.blit(textLine, (textpos[0], textpos[1] + config.currDialogSize("y") / 5))

    def showFile(self, by, to):
        pass

