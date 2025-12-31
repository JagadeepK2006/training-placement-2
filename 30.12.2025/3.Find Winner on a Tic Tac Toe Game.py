class Solution(object):
    def tictactoe(self, moves):
        grid = [['', '', ''],['', '', ''],['', '', '']]

        for x_move in range(0, len(moves), 2):
            grid[moves[x_move][0]][moves[x_move][1]] = 'X'

        for x_move in range(1, len(moves), 2):
            grid[moves[x_move][0]][moves[x_move][1]] = 'O'
        
        diag1 = (grid[0][0], grid[1][1], grid[2][2])
        diag2 = (grid[0][2], grid[1][1], grid[2][0])
        
        if set(diag1) == {'X'}:
            return 'A'
        if set(diag1) == {'O'}:
            return 'B'

        if set(diag2) == {'X'}:
            return 'A'
        if set(diag2) == {'O'}:
            return 'B'

        for row in range(3):
            if set(grid[row]) == {'O'}:
                return 'B'
            if set(grid[row]) == {'X'}:
                return 'A'    

        transposed = list(zip(*grid))

        for row in range(3):
            if set(transposed[row]) == {'O'}:
                return 'B'
            if set(transposed[row]) == {'X'}:
                return 'A'

        if len(moves) == 9:
            return 'Draw'
        return 'Pending'
