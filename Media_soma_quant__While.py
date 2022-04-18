continuar = "Ss"
soma = media = quant = maior = menor = 0
while continuar in "Ss":
    numero = int(input("Digite um número: "))
    soma += numero
    quant += 1
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    continuar = str(input("Deseja continuar? [S/N]: ")).upper().strip()
media = soma / quant
print(f"""Você digitou {quant} números, a média é {media:.2f}, 
o maior número é {maior} e o menor é {menor} """)
print("FIM")
