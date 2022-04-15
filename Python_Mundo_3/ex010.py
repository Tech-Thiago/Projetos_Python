print("=-=" * 20)
print("Inclusão Na Lista". center(60))
print("=-=" * 20)
lista = []
pos = 0
while True:
    lista.append(int(input("Digite um valor: ")))
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar ? [S/N]")).strip().upper()[0]
    if continuar == "N":
        break
print("=-=" * 20)
print(f"Você digitou {len(lista)} elemento")
lista.sort(reverse=True)
print(f"Os valores em ordem descrescente são {lista}")
if 5 in lista:
    print(f"O valor 5 faz parte da lista")
else:
    print("O valor 5 não faz parte da lista")
