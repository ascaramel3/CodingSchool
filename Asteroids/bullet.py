import pygame
from pygame import Vector2
from pygame.locals import USEREVENT

DESPAWN = USEREVENT + 2

class Bullet:
    img = pygame.image.load('Assets/bullet.png')
    img = pygame.transform.smoothscale_by(img, 0.05)
    def __init__(self, direction:Vector2, pos:Vector2):
        self.img = Bullet.img.copy()
        self.pos = pos
        self.velocity = direction * 10
        self.timer = 40

    def update(self):
        self.pos += self.velocity
        self.pos.x %= 1200
        self.pos.y %= 800
        self.timer -= 1

    def draw(self, screen):
        screen.blit(self.img, self.img.get_rect(center=self.pos))