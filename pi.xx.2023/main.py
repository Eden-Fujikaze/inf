with open("pi.txt", "r") as file:
    digs = [dig.strip() for dig in file]

def nFragCombine(startIdx: int, length: int):
    if length <= 0: return None
    if length==2:
        out = str(digs[startIdx]) + str(digs[startIdx + length - 1])
        return int(out)
    else:
        out = [int(digs[i]) for i in range(startIdx, startIdx + length)]
    return out

def isIncreasing(sequence: list) -> bool:
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return False
    return True

def isDecreasing(sequence: list) -> bool:
    for i in range(len(sequence) - 1):
        if sequence[i] <= sequence[i + 1]:
            return False
    return True

def isIncDec(seq: list) -> bool:
    for k in range(2, len(seq)-1):
        if isIncreasing(seq[:k]) and isDecreasing(seq[k:]):
            return True
    return False

twoFrags = [nFragCombine(i, 2) for i in range(len(digs) - 1)]
gtNT = [joined for joined in twoFrags if joined > 90]

counts = {frag: twoFrags.count(frag) for frag in range(100)}

maxCount = max(counts.values())
minCount = min(counts.values())

frag_max= min([frag for frag in counts if counts[frag]==maxCount])
frag_min= min([frag for frag in counts if counts[frag]==minCount])

found = []
for i in range(len(digs) - 5):
    sixSequence = nFragCombine(i, 6)
    if isIncDec(sixSequence):
        found.append((i, sixSequence))
######
startIdx = 0
longestSequence = []
longestSeqStartIdx = 0
longestSeqLen = 0
#dzialaj do konca
while startIdx < len(digs) - 2:
    #zacznij od 4 bo inaczej spotkamy ise z przedzialem [2,2)
    length = 4
    #dopoki nie przekraczasz granicy numerow oraz skoro liczby 0-9 to max dlugosc 20 bo podciagi o length 10
    while startIdx + length <= len(digs) and length<=20:
        #nowy ciag
        currentSequence = nFragCombine(startIdx, length)
        #jezeli inc dec
        if isIncDec(currentSequence):
            #jezeli dluzsze
            if len(currentSequence) > len(longestSequence):
                longestSequence = currentSequence.copy()
                longestSeqStartIdx = startIdx+1
                longestSeqLen = len(longestSequence)
        length += 1
    startIdx += 1

with open("wyniki3.txt", "w") as dest:
    dest.write(f"3.1 {len(gtNT)}\n")
    dest.write(f"3.2 {frag_min:02d} {minCount}\n")
    dest.write(f"{frag_max:02d} {maxCount}\n")
    dest.write(f"3.3 {len(found)}\n")
    dest.write(f"3.4 {longestSeqStartIdx}\n")
    for num in longestSequence:
        dest.write(f"{num}")