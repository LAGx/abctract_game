import pygame


class Track:

    def __init__(self, file = "error", by = 0):
        self.file = file
        pygame.mixer.music.load(self.file)
        pygame.mixer.music.play(-1, by)
        pygame.mixer.music.pause()

    def play(self):
        pygame.mixer.music.unpause()

    def pause(self):
        pygame.mixer.music.pause()

    def reset(self):
        pygame.mixer.music.rewind()
