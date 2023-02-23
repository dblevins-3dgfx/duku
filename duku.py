class Square:
    "An individual suduku square"
    def __init__(self, x, y):
        self.value = None
        self.coord = (x, y)

class Duku:
    "A suduku game"
    def __init__(self):
        self.board = [[Square(x, y) for y in range(9)] for x in range(9)]

    def sequentialize_row(self, row, rot):
        for square in row:
            square.value = ((square.coord[1]+rot)%9)+1

    def fillboard(self):
        for i, row in enumerate(self.board):
            rot = 3*i + int(i/3)
            self.sequentialize_row(row, rot)

