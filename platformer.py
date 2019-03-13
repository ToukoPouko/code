import pygame, time, random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        width = 100
        height = 100
        self.image = pygame.Surface((width, height))
        self.image.fill((0,0,255))
        self.rect = pygame.Rect(50, 50, 50, 50)
        self.change_y = 0.1
        self.change_x = 0 

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

def main():
    pygame.init()
    fps = 10
    clock = pygame.time.Clock()
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    surface.fill((255,255,255))
    player = Player()

    done = False

    while not done:
        player.update()

        clock.tick(fps)




if __name__ == "__main__":
    main()