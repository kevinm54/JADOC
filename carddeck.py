import numpy as np
import pygame

# SUITS = {
#     'hearts': 1,
#     'dimonds': 2,
#     'clubs': 3,
#     'spades': 4,
# }
# VALUES = {
#     'ace': 1,
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9,
#     '10': 10,
#     'jack': 11,
#     'queen': 12,
#     'king': 13,
# }
# deck_size = 52

rng = np.random.default_rng()

SUITS = {'hearts': 1}
VALUES = {'ace': 1, '2': 2, 'king': 13}
deck_size = 3

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.faceup = False
        self.rect = pygame.Rect(300, 300, 100, 162)
        self.color = [90, 130, 230]
        self.dragging = False
        self.click_pos = (None,None)
    
    def name(self):
        return self.value + '_of_' + self.suit
    
    def draw(self, win):
        # print("position:", self.position)
        pygame.draw.rect(win, self.color, self.rect)

    def click(self, pos):
        if self.rect.collidepoint(pos):
            self.dragging = True
            self.click_pos = pos
            return True
        else:
            return False
    
    def drag(self, mouse_pos):
        if self.dragging:
            dx = mouse_pos[0] - self.click_pos[0]
            dy = mouse_pos[1] - self.click_pos[1]
            self.rect.x += dx
            self.rect.y += dy
            self.click_pos = mouse_pos
    
    def release(self, pos):
        print("releasing", self.name(), "at pos", pos, "dragging=", self.dragging)
        if self.dragging:
            self.dragging = False
            dx = pos[0] - self.click_pos[0]
            dy = pos[1] - self.click_pos[1]
            self.rect.x += dx
            self.rect.y += dy
            print("moving card by:", (dx, dy))

class Stack:
    def __init__(self):
        self.cards = []
        self.count = 0
    
    def suffle(self):
        rng.shuffle(self.cards)

class Deck(Stack):
    def __init__(self):
        Stack.__init__(self)
        for suit in SUITS:
            for value in VALUES:
                self.cards.append(Card(suit, value))
        assert(len(self.cards) == deck_size) # Initialization test