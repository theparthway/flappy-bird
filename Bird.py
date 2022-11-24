import pygame

birdimg = [pygame.image.load('assets/redbird-downflap.png'), pygame.image.load('assets/redbird-midflap.png'), pygame.image.load('assets/redbird-upflap.png')]

class Bird:
    def __init__(self, x, y, g):
        self.x = x
        self.y = y
        self.g = g
        self.costume = 0

    def show(self, screen):
        screen.blit(birdimg[self.costume], (self.x, self.y))

    def jump(self):
        self.y -= 1
        self.costume += 1
        if self.costume == 3: self.costume = 0

    def gravity(self):
        self.y += self.g

    def colliding(self, ax, ay, bx, by):
        xs = [self.x, self.x + 34, self.x, self.x + 34]
        ys = [self.y, self.y, self.y + 24, self.y + 24]

        ans = False
        for i in range(4):
            if xs[i] >= ax and xs[i] <= bx:
                if ys[i] < ay or ys[i] > by:
                    ans = True

        return ans