import pygame, time, random, sys
from pygame.locals import *

class Property:

    def __init__(self, name, price, color, mortgage, house_price, rent):
        self.name = name
        self.price = price
        self.color = color
        self.mortgage = mortgage
        self.house_price = house_price
        self.rent = rent

    def buy(self, player):
        return
        

class Player:

    def __init__(self, name, money, properties, loot):
        self.name = name
        self.money = money
        self.properties = properties
        self.loot = loot

    def throw(self):
        return

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (50,80,180)


# Dimensions
screen_size = (1000,900)


board_y = 50
board_w = board_h = (screen_size[1]-2*board_y)
board_x = (screen_size[0]-board_w)/2


# Pygame initialization
pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Hello World!")

# Fill background
background = pygame.Surface(screen.get_size())
background.convert()
background.fill(BLUE)

# Displaying text
font = pygame.font.Font(None, 36)
text = font.render("Hello There", 1, (10,10,10))
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
background.blit(background, (0,0))

# Blit everything to the screen 
screen.blit(background, (0,0))
pygame.display.flip()

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        # --- Logic


        # --- Drawing
        pygame.draw.rect(screen, (0,0,0), [board_x, board_y, board_w, board_h])

        # --- Wrap-up
        clock.tick(60)

        # --- 

        pygame.display.update()

