num = 0
contador = 0
soma = 0
num = int(input("Digite o número [999 para parar]: "))
while num != 999:
    soma += num
    contador += 1
    num = int(input("Digite o número [999 para parar]: "))
print(f"Voce digitou {contador} números e soma deles é {soma}")
print("FIM")
