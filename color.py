import math
class Color:
    def __init__(self, r: int = 0, g: int = 0, b: int = 0):
        self.red = r
        self.green = g
        self.blue = b
    def __str__(self):
        return 'r: %d g: %d b: %d' % (self.red, self.green, self.blue)

def colDistance(c1, c2):
    return math.sqrt((c1.red - c2.red)**2 + (c1.green - c2.green)**2 + (c1.blue - c2.blue)**2)
