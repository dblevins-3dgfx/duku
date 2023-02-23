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

    def row_values(self, row_idx):
        return [square.value for square in self.board[row_idx] if square.value is not None]

    def col_values(self, col_idx):
        return [row[col_idx].value for row in self.board if row[col_idx].value is not None]

    def block_values(self, block_coord):
        result = []
        base = self.board[int(block_coord[0]/3)][int(block_coord[1]/3)].coord
        for i in range(3):
            for j in range(3):
                val = self.board[base[0]+i][base[1]+j].value
                if (val is not None):
                    result.append(val)
        return result

    def check_unique(self, values):
        value_set = set(values)
        return len(value_set) == len(values)
    
    def check_legal(self):
        ok = all([self.check_unique(self.row_values(r)) for r in range(9)])
        ok &= all([self.check_unique(self.col_values(c)) for c in range(9)])
        for i in range(3):
            for j in range(3):
                ok &= self.check_unique(self.block_values((i,j)))
        return ok
        


