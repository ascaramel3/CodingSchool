from common import *
from button import Button

class Game:
    def __init__(self, size, fps) -> None:
        self.clock: Clock = Clock()
        self.screen: Surface = set_mode(size)
        set_caption("~Simon~")
        self.sprites: Group = Group()
        self.running: bool = False
        self.fps = fps

        rect = Rect(0, 0, 200, 200)
        rect.bottomright = (600, 400)
        red = Button('red', rect.copy(), self.sprites)
        rect.bottomleft = (600, 400)
        green = Button('green', rect.copy(), self.sprites)
        rect.topright = (600, 400)
        blue = Button('blue', rect.copy(), self.sprites)
        rect.topleft = (600, 400)
        yellow = Button('yellow', rect.copy(), self.sprites)
        self.buttons = (red, green, blue, yellow)

        self.pattern = []
        self.input_pattern = []

    def handle_events(self) -> list[pygame.event.Event]:
        for event in (events:=pygame.event.get()):
            if event.type == QUIT: exit()
            if event.type == MOUSEBUTTONDOWN:
                for i, button in enumerate(self.buttons):
                    if button.rect.collidepoint(event.pos):
                        if self.pattern[len(self.input_pattern)] != i:
                            print("You can't defeat SIMON if you're dead! USER! Stay determined!")
                            quit()
                        self.input_pattern.append(i)

        return events

    def update(self, dt:int, events:list[pygame.event.Event]) -> None:
        self.sprites.update(events)
        if len(self.input_pattern) >= len(self.pattern) and not mouse.get_pressed()[0]:
            self.pattern.append(randint(0, 3))
            self.display_pattern()
            self.input_pattern = [] 

    def draw(self) -> None:
        self.screen.fill('black')
        self.sprites.draw(self.screen)
        display.flip()

    def gameloop(self) -> None:
        self.running = True
        dt: int = 0
        while self.running:
            self.update(dt, self.handle_events())
            self.draw()
            self.clock.tick(self.fps)
    
    def display_pattern(self):
        for button in self.buttons:
            button.deselect()
        self.draw()
        wait(200)
        for n in self.pattern:
            wait(200)
            self.buttons[n].select()
            self.draw()
            wait(200)
            self.buttons[n].deselect()
            self.draw()
            pygame.event.pump()


if __name__ == '__main__':
    Game((WIDTH, HEIGHT), FPS).gameloop()