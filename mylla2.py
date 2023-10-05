def win(symbol):
    row1 = mylla[0][0] == symbol and mylla[0][1] == symbol and mylla[0][2] == symbol
    row2 = mylla[1][0] == symbol and mylla[1][1] == symbol and mylla[1][2] == symbol
    row3 = mylla[2][0] == symbol and mylla[2][1] == symbol and mylla[2][2] == symbol

    col1 = mylla[0][0] == symbol and mylla[1][0] == symbol and mylla[2][0] == symbol
    col2 = mylla[0][1] == symbol and mylla[1][1] == symbol and mylla[2][1] == symbol
    col3 = mylla[0][2] == symbol and mylla[1][2] == symbol and mylla[2][2] == symbol

    diag1 = mylla[0][0] == symbol and mylla[1][1] == symbol and mylla[2][2] == symbol
    diag2 = mylla[0][2] == symbol and mylla[1][1] == symbol and mylla[2][0] == symbol

    return row1 or row2 or row3 or col1 or col2 or col3 or diag1 or diag2

mylla = [input() for i in range(3)]
if win('O'):
    print("Jebb")
else:
    print("Neibb")