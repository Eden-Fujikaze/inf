idx = 0
with open('napisy.txt', 'r') as file:
    for line in file:
        if len(line.strip())%2==0:
            idx += 1
print(idx)
