from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for idade in range(0, 7):
    nasc = int(input("Digite seu ano de nascimento: "))
    ano = atual - nasc
    if ano >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print(f"Das pessoas relacionadas, tivemos {totalmaior} maiores de idade", end=" ")
print(f"e {totalmenor} menores de idade.")
