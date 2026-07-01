import pygame
from pygame.locals import *
from pygame import Rect, Vector2

class Player:
    image = pygame.image.load("Assets/player.png")
    def __init__(self):
        self.pos = Vector2(600, 400)
        self.velocity = Vector2(0, 0)
        self.direction = Vector2(0, -1)
        self.image = Player.image.copy()
        self.lives = 3
 
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.velocity += self.direction
        if keys[K_LEFT]:
            self.direction.rotate_ip(-8)
            self.image = pygame.transform.rotate(Player.image, self.direction.angle_to(Vector2(0,-1)))
        if keys[K_RIGHT]:
            self.direction.rotate_ip(8)
            self.image = pygame.transform.rotate(Player.image, self.direction.angle_to(Vector2(0, -1)))   
        self.pos += self.velocity
        self.velocity *= 0.9
        self.pos.x %= 1200
        self.pos.y %= 800
        

    def draw(self, screen):
        screen.blit(self.image, self.image.get_rect(center=self.pos))

