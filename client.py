import pygame
from network import Network
import pickle
import numpy as np
pygame.font.init()
import carddeck
from game import Game

# Initialize the game window
width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Just a Deck of Cards")

def drawBackground(win):
    background_img = pygame.image.load(r'resources/felt_background.jpg')
    win.fill((50,150,60))
    # win.blit(background_img, (0,0))

def redrawWindow(win, game, p):
    drawBackground(win)
    for card in game.deck.cards:
        card.draw(win)
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player", player)
    game = Game()

    while run:
        clock.tick(60)
        # try:
        #     game = n.send("get")
        # except:
        #     run = False
        #     print("Couldn't get game")
        #     break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for card in game.deck.cards:
                    if card.click(pos):# and game.connected():
                        pass#print("clicked a card!")
            elif event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                for card in game.deck.cards:
                    card.drag(pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print("released cards")
                for card in game.deck.cards:
                    card.release(pos)

        redrawWindow(win, game, player)

def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        drawBackground(win)
        
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255,0,0))
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

if __name__ == "__main__":
    menu_screen()