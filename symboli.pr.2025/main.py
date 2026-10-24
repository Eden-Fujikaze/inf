palindromes = []

with open("symbole_przyklad.txt", "r") as file:
    rows = [row.strip() for row in file]

max_val = 0
total = 0
chars = "0123456789ABC"
squares = []

def dec_translation(translatee: str, from_which_system: int) -> int:
    reverse = translatee[::-1]
    system_vals = get_digits(from_which_system)
    total = 0
    for i in range(len(reverse)):
        candidate = reverse[i]
        total += pow(from_which_system, i) * system_vals.index(candidate)

    return total

def get_digits(system: int) -> str:
    return "o+*" if system == 3 else chars[:system]

def target_translation(dec_base: int, target_system: int) -> str:
    digits = get_digits(target_system)

    if dec_base == 0:
        return digits[0]

    final = ""
    while dec_base > 0:
        final = digits[dec_base % target_system] + final
        dec_base //= target_system

    return final

def check_for_square(table: list, x: int, y: int) -> bool:
    symbol = table[y][x]
    for dirX, dirY in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        newX, newY = x + dirX, y + dirY
        if not (0 <= newX < len(table[0]) and 0 <= newY < len(table)):
            return False
        if table[newY][newX] != symbol:
            return False
    return True

with open("wyniki2.txt", "w") as dest:
    for line in rows:
        reverse_line = line[::-1]
        if line == reverse_line:
            palindromes.append(line)
        current_line_val = dec_translation(line, 3)
        if (max_val < current_line_val):
            max_val = current_line_val
        total += current_line_val

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if check_for_square(rows, j, i):
                squares.append((i + 1, j + 1))

    dest.write("2.1\n")
    for pal in palindromes:
        dest.write(f"{pal}\n")
    dest.write("2.2\n")
    dest.write(f"{len(squares)}\n")
    for row_no, col_no in squares:
        dest.write(f"{row_no} {col_no}\n")
    dest.write(f"2.3\n{max_val} {target_translation(max_val, 3)}\n")
    dest.write(f"2.4\n{total} {target_translation(total, 3)}\n")
