class Solver:
    "A simple backtracking soduku solver"

    def legal(self, board):
        return False
    
    def complete(self, board):
        return False

    def solve(self, board):
        for x in board:
            for y in board[x]:
                if board[x][y] == 0:
                    for c in range(1,10):
                        board[x][y] = c
                        if self.legal(board):
                            if self.complete(board):
                                return True
                            return self.solve(board)
                    
                        

                            
