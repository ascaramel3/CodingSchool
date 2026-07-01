import pygame
from pygame import Surface
import json

class World:
    def __init__(self, width:int, height:int, palette:list[Surface]):
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.palette:list[Surface] = palette
    @classmethod
    def load(cls, width:int, height:int, pallete:list[Surface], filename:str):
        world = cls(width, height, pallete)
        with open(filename, 'r') as file:
            world.grid = json.load(file)
        return world

    def save(self, filename:str):
        with open(filename, 'w') as file:
            json.dump(self.grid, file)

    def draw(self, screen, tile_size:int):
        for y, row in enumerate(self.grid):
            for x, tile in enumerate(row):
                image = self.palette[tile]
                screen.blit(image, image.get_rect(topleft=(x * tile_size, y * tile_size)))
    
    def __getitem__(self, index):
        return self.grid[index]