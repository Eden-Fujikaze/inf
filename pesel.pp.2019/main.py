male = 0
female = 0
pplInListopad = 0
badPesel = []
seq = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]

with open("dane.txt", "r") as file, open("wyniki6.txt", "w") as dest:
    nums = [[int(char) for char in line.strip()] for line in file]
    for pesel in nums:
        # -- 6.1 --
        genderCode = pesel[-2]
        if genderCode % 2 == 0:
            female+=1
        else:
            male+=1
        # -- 6.2 --
        monthOfBirth = int(f"{pesel[2]}{pesel[3]}")
        if monthOfBirth > 12:
            monthOfBirth-=20
        if monthOfBirth == 11:
            pplInListopad+=1
        # -- 6.3 --
        if sum(weight * num for weight, num in zip(seq, pesel)) % 10 != 0:
            badPesel.append("".join(map(str, pesel)))
    dest.write(f"6.1 {female} {male}\n")
    dest.write(f"6.2 {pplInListopad}\n")
    dest.write(f"6.3 ")
    for pesel in badPesel:
        dest.write(f"{pesel}\n")
