listacomp = list()
listapar = list()
listaimpar = list()

while True:
    listacomp.append(int(input("Digite um número: ")))
    continuar = str(input("Quer continuar ? [S/N]")).strip().upper()[0]
    if continuar in "N":
        break
for lp, li in enumerate(listacomp):
    if li % 2 == 0:
        listapar.append(li)
    elif li % 2 == 1:
        listaimpar.append(li)
print(f"A lista Completa é {listacomp}")
print(f"A lista de pares é {listapar}")
print(f"A lista de impares é {listaimpar}")
