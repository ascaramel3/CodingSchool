from itertools import product

import pygame
import numpy as np
from piece import King, Queen, Bishop, Knight, Rook, Pawn

class Board(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.board = np.array([[None for _ in range(8)] for _ in range(8)])
        self.rect = pygame.Rect(0, 0, 800, 800)
        self.image = pygame.Surface((800, 800))
        self.pieces = pygame.sprite.Group()
        kinds = (Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)
        self.board[0] = [kind(0, col, False, self.pieces) for col, kind in enumerate(kinds)]
        self.board[1] = [Pawn(1, col, False, self.pieces) for col in range(8)]
        self.board[6] = [Pawn(6, col, True, self.pieces) for col in range(8)]
        self.board[7] = [kind(7, col, True, self.pieces) for col, kind in enumerate(kinds)]

    def update(self):
        self.draw_bg()
        self.pieces.draw(self.image)
    
    def draw_bg(self):
        dark = "#70512d"
        light = "#e6a44e"
        for x, y in product(*[range(0, 800, 100)] * 2):
            color = dark if (x + y) % 200 else light
            rect = pygame.Rect(x, y, 100, 100)
            pygame.draw.rect(self.image, color, rect)

    def __getitem__(self, *args, **kwargs):
        return self.board.__getitem__(*args, **kwargs)        

board = Board()