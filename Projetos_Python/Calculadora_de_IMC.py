import time

print("=-=-" * 20)
print("Calculadora de Índice de Massa Corporal(IMC)")
print("=-=-" * 20)
peso = float(input("Digite sua peso: "))
print("=-=-" * 20)
altura = float(input("Digite sua altura: "))
print("=-=-" * 20)
imc = (peso / (altura ** 2))
if imc < 18.5:
    print(f"Seu IMC é {imc:.2f}, logo você está Abaixo Do Peso")
elif (imc >= 18.5) and (imc < 25):
    print(f"Seu IMC é {imc:.2f}, logo você está com o Peso Ideal")
elif (imc >= 25) and (imc < 30):
    print(f"Seu IMC é {imc:.2f}, logo você está com Sobrepeso")
elif (imc >= 30) and (imc < 40):
    print(f"Seu IMC é {imc:.2f}, logo você está com Obesidade."
          f" Procure uma unidade de saúde")
elif imc >= 40:
    print(f"Seu IMC é {imc:.2f}, logo você está com Obesidade Mórbida."
          f" Procure uma unidade de saúde")
time.sleep(15)
