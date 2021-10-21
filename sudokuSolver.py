def solve_sudoku(self, board: List[List[str]]) -> None:
    def get_block(i, j):
        return 3*(i//3)+j//3

    rows, cols, blocks = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            n = board[i][j]
            rows[i].add(n)
            cols[j].add(n)
            blocks[get_block(i,j)].add(n)

    def next_empty_cell(i,j):
        j += 1
        if j == 9:
            j = 0
            i += 1
        if i == 9: return None
        if board[i][j] != '.':
            return next_empty_cell(i, j)
        else:
            return i, j

    def fill_cell(i,j):
        k = get_block(i,j)
        for n in range(1, 10):
            n = str(n)
            if n not in cols[j] and n not in rows[i] and n not in blocks[k]:
                board[i][j] = n
                rows[i].add(n)
                cols[j].add(n)
                blocks[k].add(n)

                end = next_empty_cell(i,j)
                if end == None: return True

                ni, nj = end

                # fill the next cell by backtracking
                if fill_cell(ni, nj): return True

                # this digit did not work, remove it from the cell
                board[i][j] = '.'
                rows[i].remove(n)
                cols[j].remove(n)
                blocks[k].remove(n)

        return False
    i,j = next_empty_cell(0,-1)
    fill_cell(i, j)    
 
board = [["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]
solve_sudoku(board)
