import pygame
import os

class Dragger():
    def __init__(self, board):
        self.board = board
        self.piece = None
    
    def update(self):
        if self.piece is None:
            return
        self.piece.rect.center = pygame.mouse.get_pos()

    def pickup(self, pos):
        if self.board[pos] is None:
            return
        self.piece = self.board[pos]
        