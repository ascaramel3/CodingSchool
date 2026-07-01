import pygame
from pygame import Rect, Vector2
from random import uniform, choice

class Asteroid:
    image = pygame.image.load('Assets/asteroid.png')
    def __init__(self, size, pos = None):
        self.image = Asteroid.image.copy()
        self.size = size
        self.pos=pos
        if pos is None:
            self.pos = Vector2(choice((0, 1200)), choice((0, 800)))
        self.velocity = Vector2(10/size, 0).rotate(uniform(0, 360))
        self.angle = 0
        self.angular_velocity = uniform(-5, 5)
        h = self.image.get_rect().h * size/3
        self.rect = Rect(0, 0, h, h)
        self.collidepoint = self.rect.collidepoint

    def update(self):
        self.pos += self.velocity
        self.pos.x %= 1200
        self.pos.y %= 800
        self.angle += self.angular_velocity
        self.image = pygame.transform.rotate(Asteroid.image, self.angle)
        self.image = pygame.transform.smoothscale_by(self.image, self.size/3)
        self.rect.center = self.pos

    def draw(self, screen):
        screen.blit(self.image, self.image.get_rect(center=self.pos))