import pygame
import config

class Dialog:
    line = []

    def __init__(self, dialog, file_name = "NAN"):
        pygame.font.init()
        self.file_name = file_name
        self.font = pygame.font.Font(None, 28)
        self.canvas = dialog
        file = open(self.file_name, "r")
        for line in file.readlines():
            self.line.append(line)
        file.close()

    def __textDivide(self, all_text):
        pass

    def showLine(self, text = "error: no text", pos = 0):
        textLine = self.font.render(text[:-1], 1, config.Color.text_dialog)
        textpos = textLine.get_rect()
        textpos.centerx = self.canvas.get_rect().centerx
        self.canvas.blit(textLine, (textpos[0], textpos[1] + config.currDialogSize("y") / 20+pos*20))

    def showFile(self, by, to):

        for line in range(to+1 - by):
            self.showLine(self.line[by+line-1], line)




