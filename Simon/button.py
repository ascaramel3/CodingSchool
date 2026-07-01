from common import *

class Button(Sprite):
    def __init__(self, color, rect:Rect, *groups):
        Sprite.__init__(self, *groups)
        self.color = Color(color)
        hsla = list(self.color.hsla)
        hsla[2] += 30
        self.highlight = Color(0)
        self.highlight.hsla = tuple(hsla) # type: ignore
        self.image = Surface(rect.size)
        self.image.fill(color)
        self.rect = rect

    def update(self, events):
        touching = self.rect.collidepoint(mouse.get_pos())
        if not touching:
            self.deselect()
        for event in events:
            if event.type == MOUSEBUTTONUP:
                self.deselect()
                break
            if event.type == MOUSEBUTTONDOWN and touching:
                self.select()
    
    def select(self):
        self.image.fill(self.highlight)
    
    def deselect(self):
        self.image.fill(self.color)