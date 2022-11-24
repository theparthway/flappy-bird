import pygame, sys, random
from Bird import Bird
from Pipe import Pipe
pygame.init()

size = width, height = 288, 512

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")

bg = pygame.image.load('assets/background-day.png')
pipeup = pygame.image.load('assets/pipe-green.png')
pipedown = pygame.transform.flip(pipeup, False, True)
baseimg = pygame.image.load('assets/base.png')
gameoverimg = pygame.image.load('assets/gameover.png')

bird = Bird((width - 34) / 2, (height - 24) / 2, 0.25)

pipe = Pipe(width, random.randint(100, 400), 0.2, 500)

run = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_SPACE]):
        bird.jump()
    elif (keys[pygame.K_ESCAPE]):
        sys.exit()


    if run:
        if bird.colliding(pipe.x, pipe.y - pipe.separation, pipe.x + 52, pipe.y):
            run = False

        bird.gravity()
        pipe.move()
        if pipe.x < -52:
            pipe.x = width
            pipe.y = random.randint(100, 400)
            pipe.separation -= 1
            pipe.v += 0.001
            bird.g += 0.001
        
        screen.blit(bg, (0, 0))
        bird.show(screen)
        screen.blit(pipeup, (pipe.x, pipe.y))
        screen.blit(pipedown, (pipe.x, pipe.y - pipe.separation))
        screen.blit(baseimg, (0, 400))
    else:
        screen.blit(gameoverimg, (0, 0))
    pygame.display.update()