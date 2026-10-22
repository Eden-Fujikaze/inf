palindromes = []

with open("symbole_przyklad.txt", "r") as file:
    rows = [row.strip() for row in file]

def check_for_square(table: list, x: int, y: int) -> bool:
    symbol = table[y][x]
    directions=[[-1,-1],[-1,0],[0,-1],[0,1],[1,0],[1,1],[-1,1],[1,-1]]
    tableX = len(table[0])
    tableY = len(table)
    for dirX, dirY in directions:
        newX = x+dirX
        newY = y+dirY
        if (0 < newX < tableX) and (0 < newY < tableY) and (symbol == table[newY][newX]):
            continue
        else:
            return False
    else:
        return True

for line in rows:
    reverse_line = line[::-1]
    if line == reverse_line:
        palindromes.append(line)

for i in range(len(rows)):
    for j in range(len(rows[i])):
        if check_for_square(rows, j, i):
            print(i+1, j+1)

system_key = "o+*"

def system_translation(translatee: str, which_system: int) -> int:
    reverse = translatee[::-1]
    sum = 0
    for i in range(len(reverse)):
        candidate = reverse[i]
        sum += pow(3, i) * system_key.index(candidate)
    return sum

print(system_translation("+oo", 1))