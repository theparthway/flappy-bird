import pygame, sys
from Bird import Bird
pygame.init()

size = height, width = 288, 512

run = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")

bg = pygame.image.load('assets/background-day.png')
birdimg = [pygame.image.load('assets/redbird-downflap.png'), pygame.image.load('assets/redbird-midflap.png'), pygame.image.load('assets/redbird-upflap.png')]
bird = Bird((height - 24) / 2, (width - 34) / 2)

pipeimg = pygame.image.load('assets/pipe-green.png')

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_SPACE]):
        bird.jump()
    
    bird.gravity()
    screen.blit(bg, (0, 0))
    screen.blit(birdimg[0], (bird.x, bird.y))
    pygame.display.update()

    