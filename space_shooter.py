# Pygame template

import pygame
import random
import os

##Conts

# screen
WIDTH = 480
HEIGHT = 600
FPS = 60
# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# game init - ready
pygame.init()

# sound init
pygame.mixer.init()

# window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Game')
clock = pygame.time.Clock()

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 45))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.rect.x += -4
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 4
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -20 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


# all sprites
all_sprites = pygame.sprite.Group()
player = Player()
mobs = pygame.sprite.Group()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

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
