b = 0
s = 0
for c in range(1, 7):
    num = int(input(f"Digite o valor {c} número: "))
    if num % 2 == 0:
        b += num
        s += 1
print(f"Digite {s}, {b}")
