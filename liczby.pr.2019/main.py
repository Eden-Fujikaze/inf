from math import factorial, gcd

def is_power_of_three(num: int) -> bool:
    while num > 1 and num%3==0:
        num//=3
    return num == 1

with open("liczby.txt", "r") as file:
    rows = [int(row.strip()) for row in file]

powers_of_three = []
factorial_sums = []
best = []
current = []

for value in rows:
    if is_power_of_three(value):
        powers_of_three.append(value)
    num_sum = sum(factorial(int(digit)) for digit in str(value))
    if value == num_sum:
        factorial_sums.append(value)

    while current and gcd(*current, value) == 1:
        current.pop(0)
    current.append(value)

    if len(current) > len(best):
        best = current[:]
nwd_highest = gcd(*best)
with open("wyniki4.txt", "w") as dest:
    dest.write(f"4.1 {len(powers_of_three)}\n")
    dest.write("4.2 ")
    for number in factorial_sums:
        dest.write(f"{number}\n")
    dest.write(f"4.3 {best[0]} {len(best)} {nwd_highest}\n")