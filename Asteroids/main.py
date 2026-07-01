from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import random
import pygame
from pygame import Surface, Color
from pygame.time import Clock
from pygame.event import Event
from pygame.locals import QUIT, USEREVENT
from player import Player
from asteroid import Asteroid
from sys import exit

pygame.init()
FPS: int = 30
screen: Surface = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("~Asteroids: Rainbow Epilepsy Bongo Cat Edition 2025 (Epilepsy Warning)~")
clock: Clock = Clock()

color = Color(200,0,0)
player = Player()
asteroids = []
SPAWN = USEREVENT + 1
pygame.time.set_timer(SPAWN, 2000)

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
        if event.type == SPAWN:
            asteroids.append(Asteroid(random.randint(1,3)))
    return events

def update(events: list[Event]) -> None:
    player.update()
    for asteroid in asteroids:
        asteroid.update()
    
    hue = color.hsla[0] + 3
    hue %= 255
    color.hsla = (hue, *color.hsla[1:])

def draw() -> None:
    screen.fill(color)
    player.draw(screen)
    for asteroid in asteroids:
        asteroid.draw(screen)
    pygame.display.flip()

        
main()