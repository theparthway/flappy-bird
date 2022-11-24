class Pipe:
    def __init__(self, x, y, v, separation):
        self.x = x
        self.y = y
        self.v = v
        self.separation = separation

    def move(self):
        self.x -= self.v