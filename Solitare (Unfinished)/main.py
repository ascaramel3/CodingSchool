import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from pygame import Rect
import sys
from card import *
from deck import Deck
from dragger import dragger
pygame.init()

FPS = 30
WIDTH: int = 1200
HEIGHT: int = 800

class Cell:
    def __init__(self, pos, cards=()):
        self.hitbox: Rect = Rect(pos, Card.SIZE)
        self.cards: list[Card] = [card for card in cards]
    
    def push(self, card:Card):
        self.cards.append(card)
        card.rect.topright = self.hitbox.topright
        self.hitbox.y += 20
        card.face_up = True
        return True
    
    def pop(self):
        self.hitbox.y -= 20
        return self.cards.pop()

hand = Cell((10, 50 + Card.SIZE.y))
deck = Deck((10, 10))
cells = [Cell((40 + (Card.SIZE.x + 10) * (i + 1), 10 )) for i in range(7)]

for i in range(7):
    for cell in cells[i:]:
        cell.push(deck.cards.pop())

class Game:
    def __init__(self) -> None:
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Solitaire")

    def handle_events(self) -> list[pygame.event.Event]:
        events: list[pygame.event.Event] = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if deck.rect.collidepoint(event.pos):
                    deck.draw_card(hand)
                    continue
                for cell in cells + [hand]:
                    for card in cell.cards:
                        if not cell.hitbox.collidepoint(event.pos):
                            continue
                    if dragger.card:
                        dragger.place(cell)
                    else:
                        dragger.pickup(cell)
                    break
                else:
                    dragger._return()
                
        return events    

    def update(self) -> None:
        pass

    def draw(self) -> None:
        self.screen.fill('darkgreen')
        for card in deck.cards + hand.cards:
            self.screen.blit(card.image, card.rect)
        for cell in cells:
            for card in cell.cards:
                self.screen.blit(card.image, card.rect)
        
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