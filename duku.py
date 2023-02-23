class Square:
    "An individual suduku square"
    def __init__(self, x, y):
        self.value = None
        self.coord = (x, y)

class Duku:
    "A suduku game"
    def __init__(self):
        self.board = [[Square(x, y) for y in range(9)] for x in range(9)]
