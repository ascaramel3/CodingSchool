import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import sys
from player import Player

pygame.init()

FPS = 30
WIDTH: int = 1200
HEIGHT: int = 800

class Game:
    def __init__(self) -> None:
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("--template--")
        self.sprites = pygame.sprite.Group()
        self.player = Player()

    def handle_events(self) -> list[pygame.event.Event]:
        events: list[pygame.event.Event] = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
        return events

    def update(self) -> None:
        keys = pygame.key.get_pressed

    def draw(self) -> None:
        self.screen.fill('white')
        self.player.draw(self.screen)

        pygame.display.flip()

    def gameloop(self) -> None:
        while True:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.gameloop()