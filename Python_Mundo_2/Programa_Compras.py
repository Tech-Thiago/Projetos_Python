print("=-=-" * 15)
titulo = "Programa"
print(titulo.center(50))
print("=-=-" * 15)

cont = 0
total = 0
produtos = 0
tot = 0
menor = 0
while True:
    nome = str(input("Digite o nome do produto: ")).strip().upper()
    preco = int(input("Digite o preço: R$ "))
    cont += 1
    total += preco
    if preco > 1000:
        tot += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Irá continuar ? [S/N]")).strip().upper()
    if continuar == "N":
        break
print(f"""O total gasto na compra é de R$ {total}
A quantidade de produtos que custam mais de R$1000 reais são {tot} 
O nome do produto mais barato é {menor}""")
