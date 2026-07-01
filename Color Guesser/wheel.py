import pygame
from pygame import MOUSEBUTTONDOWN, Vector2, Color
from itertools import product


class Wheel:
    def __init__(self, center, r):
        self.center = center
        self.r = r
        self.hue = 0
        self.saturation = 0

    def update(self, events):
       pos = Vector2(pygame.mouse.get_pos())
       clicking = any(event.type == MOUSEBUTTONDOWN for event in events)

       if clicking and pos.distance_to(self.center) <= self.r:
            self.drag = True
       if not pygame.mouse.get_pressed()[0]:
            self.drag = False
       if self.drag:
            r, angle = (pos - self.center).as_polar()
            self.hue = int(angle) % 360
            self.saturation = int(pygame.math.clamp(r / self.r * 100, 0, 100))

    def draw(self, screen, value):
        color = Color(0)
        for angle, r in product(range(360), range(1, self.r)):
            point = Vector2.from_polar((r, angle))
            point += self.center
            r = r / self.r * 100
            color.hsva = (angle, r, value, 100)
            pygame.draw.circle(screen, color, point, 10)
        point = self.center + Vector2.from_polar((self.saturation / 100 * self.r, self.hue))
        pygame.draw.circle(screen, 'black', point, 8)
        pygame.draw.circle(screen, 'white', point, 4)