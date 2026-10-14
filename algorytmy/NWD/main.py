def NWD(a: int, b:int) -> int:
    while (b!=0):
        temp = a
        a = b
        b = temp % b
    return a

print(NWD(125,300))