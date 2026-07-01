import pygame
from pygame import Vector2, Rect, Surface

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image = Surface((80, 80))
        self.rect = self.image.get_rect(center = (600, 400))
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)