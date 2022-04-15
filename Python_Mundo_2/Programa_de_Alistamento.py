from datetime import date
import time

print("=-=-" * 20)
print("Programa de Alistamento")
print("=-=-" * 20)
atual = date.today().year
data_nas = int(input("Ano de nascimento: "))
idade = atual - data_nas
print("=-=-" * 20)
print(f"Quem nasceu em {data_nas}, tem {idade} anos em {atual}")
print("=-=-" * 20)
print("""Qual o seu sexo: 
[1] Feminino
[2] Masculino """)
print("=-=-" * 20)
numero = int(input("Digite o número correspondente: "))
print("=-=-" * 20)
if numero == 1:
    print("Você não precisa se alistar")
elif idade == 18 and numero == 2:
    print(f"VOCÊ TERÁ QUE SE ALISTAR IMEDIATAMENTE")
elif idade < 18 and numero == 2:
    saldo1 = 18 - idade
    print(f"Seu alistamente será em {saldo1} anos ")
elif idade > 18 and numero == 2:
    saldo2 = idade - 18
    print(f"Você deveria ter se alistado há {saldo2} ano.")
time.sleep(20)
