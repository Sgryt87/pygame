# Pygame template

import pygame
import random
import os

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
# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

print(img_folder)


class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # render img from folder & convert for the
        self.image = pygame.image.load(os.path.join(img_folder, 'p1_jump.png')).convert()
        # disable img back background
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed

        if self.rect.left > WIDTH:
            self.rect.right = 0

        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5

        if self.rect.top < 200:
            self.y_speed = 5


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
    screen.fill(RED)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame, quit()
