import pygame
from pygame import MOUSEBUTTONDOWN, Rect, Surface, Color, Vector2

class Slider:
    def __init__(self, rect):
        self.rect = rect
        self.value = 100
        self.drag = False

    def update(self, events):
        pos = Vector2(pygame.mouse.get_pos())
        clicking = any(event.type == MOUSEBUTTONDOWN for event in events)

        if clicking and self.rect.collidepoint(pos):
            self.drag = True
        if not pygame.mouse.get_pressed()[0]:
            self.drag = False
        if self.drag:
            self.value = (pos.x - self.rect.x) / self.rect.w * 100
            self.value = int(pygame.math.clamp(self.value, 0, 100))


    def draw(self, screen, h, s):
        color = Color(0)
        for v in range(101):
            color.hsva = (h, s, v, 100)
            rect = self.rect.copy()
            rect.w //= 100
            rect.x += v * rect.w

            pygame.draw.rect(screen, color, rect)

        rect = self.rect.copy()
        rect.w //= 15
        rect.h *= 0.8
        rect.y += rect.h * 0.1
        left = self.rect.left + rect.w/2
        right = self.rect.right - rect.w/2
        rect.centerx = pygame.math.lerp(left, right, self.value/100)
        pygame.draw.rect(screen, 'white', rect)