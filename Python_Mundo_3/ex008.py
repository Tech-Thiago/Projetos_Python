lista = []
while True:
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
        print(f"Valor {n} adicionado com sucesso...")
    else:
        print("Valores duplicados")
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if continuar == "N":
        break
lista.sort()
print(f"Os números obtidos são: {lista}")
