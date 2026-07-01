from card import Card
from pygame.mouse import get_pos

class Dragger:
    def __init__(self):
        self.card: Card | None = None
        self.cell = None
    def update(self):
        if self.card is None:
            return
        self.card.rect.center = get_pos()
    
    def pickup(self, cell):
        if not cell.cards:
            return
        self.card = cell.pop()
        self.cell = cell

    def place(self, cell):
        if not self.card:
            return
        cell.push(self.card)
        self.card = None
        self.cell = None
    
    def _return(self):
        self.place(self.cell)

dragger = Dragger()
