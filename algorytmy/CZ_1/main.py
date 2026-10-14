def rozklad(num: int) -> list[int]:
    rozlozone = []
    for i in range(2,num+1):
        while(num%i)==0:
            num//=i
            rozlozone.append(i)
        if num==1:
            break
    return rozlozone

print(rozklad(1200000000))