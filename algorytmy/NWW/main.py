# NmWW / x AND NmWW / y

def NWW(a: int, b: int) -> int:
    for i in range(1,b+1):
        if ((a*i)%b) == 0:
            return a*i
    return None

print(NWW(15,25))