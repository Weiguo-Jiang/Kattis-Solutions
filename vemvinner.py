row1 = input().split()
row2 = input().split()
row3 = input().split()

def get_row_winner(row):
    if row[0] == row[1] == row[2]:
        return row[0]
    return None

def get_col_winner(row1, row2, row3, col):
    if row1[col] == row2[col] == row3[col]:
        return row1[col]
    return None

def get_diag_winner(row1, row2, row3):
    if row1[0] == row2[1] == row3[2]:
        return row1[0]
    if row1[2] == row2[1] == row3[0]:
        return row1[2]
    return None

def get_winner(row1, row2, row3):
    winner = get_row_winner(row1)
    if winner:
        return winner
    winner = get_row_winner(row2)
    if winner:
        return winner
    winner = get_row_winner(row3)
    if winner:
        return winner
    winner = get_col_winner(row1, row2, row3, 0)
    if winner:
        return winner
    winner = get_col_winner(row1, row2, row3, 1)
    if winner:
        return winner
    winner = get_col_winner(row1, row2, row3, 2)
    if winner:
        return winner
    winner = get_diag_winner(row1, row2, row3)
    if winner:
        return winner
    return None

winner = get_winner(row1, row2, row3)
if winner == 'X':
    print("Johan har vunnit")
elif winner == 'O':
    print("Abdullah har vunnit")
else:
    print("ingen har vunnit")