idxO=0
idxZ=0
with open('napisy.txt', 'r') as file:
    for line in file:
        line = line.strip()
        Same = True
        for i in range(len(line)):
            value = line[i];
            if value != line[0]:
                Same = False
                break
        if Same:
            match line[0]:
                case "1":
                    idxO+=1
                case "0":
                    idxZ+=1
                case _:
                    pass
print(idxZ, idxO)
