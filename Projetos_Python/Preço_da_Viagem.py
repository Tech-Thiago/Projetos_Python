viagem = float(input("Quantos km será percorrido:  "))
print(f"Você está prestes a percorrer {viagem} km ")
preço = viagem * 0.50
if viagem <= 200:
    print(preço)
if viagem > 200:
    multa1 = viagem * 0.45
    print(multa1)