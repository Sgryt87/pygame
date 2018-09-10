# Pygame template

import pygame
import random

##Conts
# screen
WIDTH = 800
HEIGHT = 600
FPS = 30
# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


# game init - ready
pygame.init()

# sound init
pygame.mixer.init()

# window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Game')
clock = pygame.time.Clock()

# all sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game Loop
running = True

while running:
    # keep loop running at the right speed
    # clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        # check window close
        if event.type == pygame.QUIT:
            running = False
    # update
    all_sprites.update()
    # draw/render
    # after  drawing everything, flip the display (when back end rendering is done, return a final view
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame, quit()
