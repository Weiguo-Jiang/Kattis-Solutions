d = dict()
def solve(board, cnt):
    b = ''.join(board)
    if b in d:
        return d[b]
    legal_moves = []
    for i in range(len(board)):
        if board[i] == 'o':
            if i > 1 and board[i-1] == 'o' and board[i-2] == '-':
                legal_moves.append((i, i-1, i-2))
            if i < len(board)-2 and board[i+1] == 'o' and board[i+2] == '-':
                legal_moves.append((i, i+1, i+2))
    if not legal_moves:
        return cnt
    else:
        min_pebbles = 100
        for move in legal_moves:
            new_board = board[:]
            new_board[move[0]] = '-'
            new_board[move[1]] = '-'
            new_board[move[2]] = 'o'
            min_pebbles = min(min_pebbles, solve(new_board, cnt-1))
        d[b] = min_pebbles
        return min_pebbles

n = int(input())
for _ in range(n):
    board = [c for c in input()]
    print(solve(board, board.count('o')))