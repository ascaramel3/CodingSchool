from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from pygame import Surface
from pygame.time import Clock
from pygame.event import Event
from pygame.locals import QUIT, KEYDOWN, K_s
from pygame.math import clamp
from sys import exit
import json
from world import World

pygame.init()
FPS: int = 30
screen: Surface = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Platformer Map Builder")
clock: Clock = Clock()

tile = 1
TILE_SIZE = 80
FILENAME = 'world_data.json'
WIDTH = 800 // TILE_SIZE
HEIGHT = 800 // TILE_SIZE

palette = [Surface((80, 80)) for _ in range(3)]
palette[0].fill('dodgerblue')
palette[1].fill('white')
palette[2].fill('palevioletred1')
world: World


def main() -> None:
    global world
    try:
        print('starting')
        world = World.load(10, 10, palette, FILENAME)
    except FileNotFoundError:
        world = World(100, 100, palette)
    while True:
        clock.tick(FPS)
        update(handle_events())
        draw()

def handle_events() -> list[Event]:
    global tile
    events: list[Event] = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.unicode.isnumeric():
                tile = clamp(int(event.unicode) - 1, 0, len(palette) - 1)
            if event.key == K_s:
                world.save(FILENAME)
                print("World has been saved.")
    return events

def update(events: list[Event]) -> None:
    if pygame.mouse.get_pressed()[0]:
        col, row = pygame.mouse.get_pos()
        col = clamp(col, 1, 799)
        row = clamp(row, 1, 799)
        col //= TILE_SIZE
        row //= TILE_SIZE
        world[row][col] = tile

def draw() -> None:
    screen.fill('white')
    world.draw(screen, 80)
    
    pygame.display.flip()

        
main()