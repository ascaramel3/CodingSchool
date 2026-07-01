import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame import Rect, Vector2
from pygame.font import Font
import sys

from slider import Slider
from wheel import Wheel
from pygame.color import THECOLORS
from random import choice

pygame.init()
pygame.font.init()

FPS = 30
WIDTH: int = 800
HEIGHT: int = 800
font = Font(None, 30)

class Game:
    def __init__(self) -> None:
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Color Guesser")
        self.sprites = pygame.sprite.Group()
        self.slider = Slider(Rect(0, 0, 400, 100))
        self.wheel = Wheel(Vector2(400, 400), 200)
        self.font_color_name = choice(tuple(THECOLORS.keys()))
        self.color = THECOLORS[self.font_color_name]
        self.button = Rect(0, 0, 100, 50)
        self.button.center = (400, 720)
        self.button_text = "I'm done!"
        self.button_color = 'chartreuse4'
        self.score = None

    def handle_events(self) -> list[pygame.event.Event]:
        events: list[pygame.event.Event] = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and self.button.collidepoint(event.pos):
                if self.score is None:
                    self.score = self.evaluate()
                    self.button_text = "Restart"
                    self.button_color = "gray47"
                else:
                    self.score = None
                    self.font_color_name = choice(tuple(THECOLORS.keys()))
                    self.color = THECOLORS[self.font_color_name]
                    self.button_text = "I'm done!"
                    self.button_color = "chartreuse4"
        return events

    def update(self, events) -> None:
        self.slider.update(events)
        self.wheel.update(events)

    def draw(self) -> None:
        self.screen.fill('black')
        if self.score is None:
            self.slider.draw(self.screen, self.wheel.hue, self.wheel.saturation)
            self.wheel.draw(self.screen, self.slider.value)
            color = pygame.Color(1)
            color.hsva = (self.wheel.hue, self.wheel.saturation, self.slider.value, 100)
            text = font.render(self.font_color_name, True, color)
            self.screen.blit(text, text.get_rect(center=(400, 650)))
            
        else:
            if self.score > 80:
                text = font.render(f"Your score is {self.score:.2f}% of the color. Good job!", True, 'white')
            else:
                text = font.render(f"Your score is {self.score:.2f}% of the color.", True, 'white')
            self.screen.blit(text, text.get_rect(center=(400, 400)))
        pygame.draw.rect(self.screen, self.button_color, self.button)
        text = font.render(self.button_text, True, 'white')
        self.screen.blit(text, text.get_rect(center=self.button.center))    
        pygame.display.flip()

    def gameloop(self) -> None:
        while True:
            self.clock.tick(FPS)
            self.update(self.handle_events())
            self.draw()
    
    def evaluate(self):
        h, s, v, _ = pygame.Color(self.color).hsva
        hue_score = abs(h - self.wheel.hue)
        if hue_score > 180:
            hue_score = 360 - hue_score
        hue_score *= 100/180
        saturation_score = 100 - abs(self.wheel.saturation - s)
        value_score = 100 - abs(self.slider.value - v)
        return sum((hue_score, saturation_score, value_score)) / 3

if __name__ == '__main__':
    game = Game()
    game.gameloop()