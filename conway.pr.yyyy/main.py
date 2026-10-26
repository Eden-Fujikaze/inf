from itertools import product
with open("gra.txt", "r") as game:
    rows = [row.strip() for row in game]
n = len(rows[2])
m = len(rows)
temp_board = rows.copy()

def check_neighbours(board: list, x: int, y: int) -> int:
    neighbours = []
    directions = product([-1,0,1], repeat = 2)
    for dirY, dirX in directions:
        if dirX == 0 and dirY == 0:
            continue
        newX = (x+dirX)%n
        newY = (y+dirY)%m
        subject = board[newY][newX]
        neighbours.append(subject)
    return neighbours.count("X")

def step(board: list):
    new_board=[]
    for i in range(m):
        row = ""
        for j in range(n):
            count = check_neighbours(board, j, i)
            self = board[i][j]
            if self == "." and count == 3:
                row+="X"
            elif self == "X" and 2 <= count <= 3:
                row += "X"
            else:
                row += "."
        new_board.append(row)
    return new_board

with open("wyniki_5.txt", "w") as dest:
    board = rows
    for _ in range(36):
        board = step(board)
    dest.write(f"5.1 {check_neighbours(board, 18, 1)}\n")
    dest.write(f"5.2 {sum(row.count("X") for row in step(rows))}\n")
    board = rows
    for generation in range(2, 101):
        new = step(board)
        if new == board:
            dest.write(f"5.3 {generation} {sum(row.count("X") for row in new)}")
            break
        board = new