n = (int(input("Digite um valor: ")),
     int(input("Digite outro valor: ")),
     int(input("Digite mais um valor: ")),
     int(input("Digite mais um outro valor: ")))
print("=-=-" * 15)
print(f"Esses são os valores escolhidos {n}")
print("=-=-" * 15)
print(f"O valor 9 apareceu -> {n.count(9)} vezes")
print("=-=-" * 15)
if 3 in n:
    print(f"O valor 3 apareceu na posição -> {n.index(3) + 1}°")
else:
    print("O valor 3 não foi encontrado")
print("=-=-" * 15)
print("Os números pares são -> ", end="")
for num in n:
    if num % 2 == 0:
        print(f"{num}", end=" ")
