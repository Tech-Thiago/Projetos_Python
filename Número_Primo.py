n1 = int(input("Digite um número: "))
tot = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print("\033[1;33m", end=" ")
        tot += 1
    else:
        print("\033[1;31m", end=" ")
    print(f"\n{c}")
print(f"\033[1;36mO numero {n1} foi divisivel {tot} vezes\033[m")
if tot == 2:
    print("\033[1;31mNúmero primo")
else:
    print("\033[1;35mNão é número primo")
