# k pos1 pos2 pos3 ...
# 2 ...  ...  ...  ...
# 3 ...
# .
numDict = {k: 0 for k in range(2,17)}
with open('napisy.txt', 'r') as file:
    for line in file:
        line=line.strip()
        numDict[len(line)]+=1

print(numDict)
