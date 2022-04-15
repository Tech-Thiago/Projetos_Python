cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input("Digite um número de 0 a 20: "))
    if 0 <= num <= 20:
        print(f"Você digitou o número {cont[num]}")
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Você quer continuar ? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
print("Fim do Programa")
