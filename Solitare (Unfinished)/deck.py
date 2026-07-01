from itertools import product
from card import Card, Rank, Suit
from random import shuffle
import pygame
from pygame import Rect
from pygame import Vector2

class Deck:
    def __init__(self, pos):
        self.group = pygame.sprite.Group()
        self.pos = Vector2(pos)
        self.discard: list[Card] = []  
        self.cards = [Card(Rank(rank), suit, self.group) for rank, suit in product(range(1, 14), Suit)]
        shuffle(self.cards)
        self.reset()

    def draw_card(self, hand):
        while hand.cards:
           self.discard.append(hand.pop())
        
        if len(self.cards) == 0:
            self.cards = self.discard
            self.reset()
            self.discard = []

        for _ in range(3):
            if not self.cards:
                break
            hand.push(self.cards.pop())
    
    def reset(self):
        for i, card in enumerate(self.cards):
            card.face_up = False
            card.rect.topleft = ((10 + self.pos.x +  i//3, 10 + self.pos.y + i//3))
        self.rect = Rect(self.pos, self.cards[0].rect.size)
    
    def draw(self, screen):
        self.group.draw(screen)