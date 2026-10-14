dict2 = {}

with open("nowe.txt", "r") as nowe, open("slowa.txt", "r") as slowa, open("wynik5.txt", "w") as ans:
    slowaList = [row.strip() for row in slowa]
    noweList = [row.strip() for row in nowe]
    dict3 = {k: [0,0] for k in noweList}

    for row in slowaList:
        if row in dict3:
            dict3[row][0] += 1
        reversed_row = row[::-1]
        if reversed_row in dict3:
            dict3[reversed_row][1] +=1
        if len(row) in dict2:
            dict2[len(row)] += 1
        else:
            dict2[len(row)] = 1

    ans.write("4.1 ")
    for key in dict2:
        val = dict2[key]
        ans.write(f"{key} {val}\n")


