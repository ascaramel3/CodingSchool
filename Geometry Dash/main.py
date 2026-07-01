from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from pygame import Surface
from pygame.time import Clock
from pygame.event import Event
from pygame.locals import QUIT
from sys import exit

pygame.init()
FPS: int = 30
screen: Surface = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("--template--")
clock: Clock = Clock()

def main() -> None:
    while True:
        clock.tick(FPS)
        update(handle_events())
        draw()

def handle_events() -> list[Event]:
    events: list[Event] = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            exit()
    return events

def update(events: list[Event]) -> None:
    pass

def draw() -> None:
    screen.fill('white')
    
    pygame.display.flip()

        
main()
    