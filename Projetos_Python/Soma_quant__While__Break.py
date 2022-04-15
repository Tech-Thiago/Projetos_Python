numero = soma = cont = 0
while True:
    numero = int(input("Digite um valor [999 para parar]: "))
    if numero == 999:
        break
    cont += 1
    soma += cont
print(f"A quantidade de numero é {cont} e a soma é {soma}")
