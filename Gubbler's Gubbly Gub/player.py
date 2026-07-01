import pygame

class Player:
    def __init__(self):
        self.img = pygame.image.load("Textures/player.png")
        self.dest = (400, 600)
    def update(self, screen):
        screen.blit(self.img, self.dest)
        
