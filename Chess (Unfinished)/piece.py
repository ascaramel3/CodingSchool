import pygame
import os
from pygame import Rect

images = {}
for kind in ('king', 'queen', 'bishop', 'knight', 'rook', 'pawn'):
    images[f'white{kind}'] = pygame.image.load(f'assets/white{kind}.png')
    images[f'black{kind}'] = pygame.image.load(f'assets/black{kind}.png')
    images[f'white{kind}'] = pygame.transform.smoothscale(images[f'white{kind}'], (100, 100))
    images[f'black{kind}'] = pygame.transform.smoothscale(images[f'black{kind}'], (100, 100))

class Piece(pygame.sprite.Sprite):
    def __init__(self, row, col, is_white, *groups):
        super().__init__(*groups)
        self.pos = (row, col)
        self.is_white = is_white
        self.image = images[('white' if is_white else 'black') + type(self).__name__.lower()]
        self.rect = Rect(col * 100, row * 100, 100, 100)
        

class King(Piece):
    def __init__(self, row, col, is_white, *groups):
        super().__init__(row, col, is_white, *groups)

class Queen(Piece):
    def __init__(self, row, col, is_white, *groups):
        super().__init__(row, col, is_white, *groups)

class Bishop(Piece):
    def __init__(self, row, col, is_white, *groups):
        super().__init__(row, col, is_white, *groups)

class Knight(Piece):
    def __init__(self, row, col, is_white, *groups):
        super().__init__(row, col, is_white, *groups)

class Rook(Piece):
    def __init__(self, row, col, is_white, *groups):
        super().__init__(row, col, is_white, *groups)

class Pawn(Piece):
    def __init__(self, row, col, is_white, *groups):
        super().__init__(row, col, is_white, *groups)