best = (9, float('inf'))
def legal_moves(board, pegs):
    legal_moves = []
    for peg in pegs:
        # check left
        if peg % 9 > 1 and board[peg-1] == 'o' and board[peg-2] == '.':
            legal_moves.append((peg, peg-1, peg-2))
        # check right
        if peg % 9 < 7 and board[peg+1] == 'o' and board[peg+2] == '.':
            legal_moves.append((peg, peg+1, peg+2))
        # check up
        if peg > 17 and board[peg-9] == 'o' and board[peg-18] == '.':
            legal_moves.append((peg, peg-9, peg-18))
        # check down
        if peg < 27 and board[peg+9] == 'o' and board[peg+18] == '.':
            legal_moves.append((peg, peg+9, peg+18))
    return legal_moves

def recursion(board, pegs, peg_cnt, move_cnt):
    moves = legal_moves(board, pegs)

    if len(moves) == 0:
        global best
        if peg_cnt < best[0] or (peg_cnt == best[0] and move_cnt < best[1]):
            best = (peg_cnt, move_cnt)
        return

    for move in moves:
        board_copy = [b for b in board]

        board_copy[move[0]] = '.'
        board_copy[move[1]] = '.'
        board_copy[move[2]] = 'o'

        pegs_copy = [p for p in pegs]
        pegs_copy.remove(move[0])
        pegs_copy.remove(move[1])
        pegs_copy.append(move[2])

        recursion(board_copy, pegs_copy, peg_cnt-1, move_cnt+1)


N = int(input())
for i in range(N):

    board = []

    # get initial board, dimension 5x9
    for j in range(5):
        for k in input():
            board.append(k)

    # empty line after each board except the last board
    if i != N-1:
        input()

    # get initial peg indices
    pegs = []
    for j in range(len(board)):
        if board[j] == 'o':
            pegs.append(j)

    # get initial peg count
    peg_cnt = len(pegs)

    # get initial move count
    move_cnt = 0

    # get best solution
    recursion(board, pegs, peg_cnt, move_cnt)

    # print best solution
    print(best[0], best[1])
    best = (9, float('inf'))