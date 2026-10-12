def dopisz(title: str,character: str) -> str:
    return title + character

def zmien(title: str,character: str) -> str:
    return title[:-1] + character

def usun(title: str) -> str:
    return title[:-1]

def przesun(title: str,character: str) -> str:
    first_occurence = title.index(character)
    ascii_code = ord(title[first_occurence])
    if title[first_occurence]=="Z":
        new_char = "A"
    else:
        new_char = chr(ascii_code+1)
    title = title[:first_occurence] + new_char + title[first_occurence+1:]
    return title

def checkStreak(instructions: list[str]) -> tuple[str, int]:
    best_name, best_streak = "", 0
    cur_name, cur_streak = "", 0
    for el in instructions:
        if el == cur_name:
            cur_streak += 1
        else:
            cur_name, cur_streak = el, 1
        if cur_streak > best_streak:
            best_name, best_streak = cur_name, cur_streak
    return best_name, best_streak

with open("instrukcje.txt", "r") as file, open("wyniki4.txt", "w") as dest:
    rows = [line.strip().split() for line in file]
    title = ""
    charCount = {}
    for command in rows:
        instruction = command[0]
        arg = command[1]
        match instruction:
            case "DOPISZ":
                title = dopisz(title, arg)
                charCount[arg] = charCount.get(arg, 0) + 1
            case "ZMIEN":
                title = zmien(title, arg)
            case "USUN":
                title = usun(title)
            case "PRZESUN":
                title = przesun(title, arg)
            case _:
                pass
    mostFrequentChar = max(charCount, key=charCount.get)
    name, streak = checkStreak([row[0] for row in rows])
    dest.write(f"4.1 {len(title)}\n")
    dest.write(f"4.2 {name} {streak}\n")
    dest.write(f"4.3 {mostFrequentChar} {charCount[mostFrequentChar]}\n")
    dest.write(f"4.4 {title}")