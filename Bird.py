class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def jump(self):
        self.y -= 2

    def gravity(self):
        self.y += 0.3