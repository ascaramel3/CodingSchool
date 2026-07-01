import pygame
from pygame.sprite import Sprite
from enum import StrEnum, auto
from pygame import Vector2, Rect, Surface

class Rank:
    def __init__(self, n:int):
        self.n = n
    
    def __str__(self) -> str:
        strings = {1:'ace', 11:'jack', 12:'queen', 13:'king'}
        return strings.get(self.n, str(self.n))

class Suit(StrEnum):
    SPADES = auto()
    CLUBS = auto()
    HEARTS = auto()
    DIAMONDS = auto()

class Card(Sprite):
    SIZE = Vector2(100, 145)
    back = pygame.image.load('Other Textures/backside_of_card.png')
    back = pygame.transform.smoothscale(back, SIZE)
    def __init__(self, rank:Rank, suit:Suit, *groups):
        super().__init__(*groups)
        self.rank: Rank = rank
        self.suit: Suit = suit
        self._face_up: bool = False 
        self.face = pygame.image.load(f'Card Textures/{self.rank}_of_{self.suit}.png')
        self.face = pygame.transform.smoothscale(self.face, Card.SIZE)
        self.image: Surface = self.back
        self.rect: Rect = self.image.get_rect()
    
    @property
    def face_up(self):
        return self._face_up

    @face_up.setter
    def face_up(self, value:bool) -> None:
        self._face_up = value
        if value:
            self.image = self.face
        else:
            self.image = Card.back