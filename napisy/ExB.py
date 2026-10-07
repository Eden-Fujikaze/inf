idx = 0
with open('napisy.txt', 'r') as file:
    for line in file:
        idxZ=0
        idxO=0
        for i in range(len(line)):
            value = line[i];
            match value:
                case "0":
                    idxZ+=1
                case "1":
                    idxO +=1
                case _:
                    pass
            if idxZ==idxO:
                idx+=1
print(idx)
