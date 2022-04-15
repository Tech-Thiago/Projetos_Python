import random
import time

itens = ("Papel", "Pedra", "Tesoura")
maquina = int(random.uniform(0, 2))
print("""Escolha uma opção
[0]Papel
[1]Pedra
[2]Tesoura""")
player = int(input("Digite a opção: "))
time.sleep(1.2)
print("JO")
time.sleep(1.2)
print("KEN")
time.sleep(1.2)
print("PÔ!!")
time.sleep(0.3)
print("=-=-" * 20)
print(f"Computador jogou {(itens[maquina])}")
print(f"jogador jogou {(itens[player])}")
print("=-=-" * 20)
if maquina == 0:
    if player == 0:
        print("Deu Empate, jogue novamente! ")
    elif player == 1:
        print("Você perdeu, jogue novamente! ")
    elif player == 2:
        print("Você ganhou!!")
    else:
        print("Jogada Inválida!")
elif maquina == 1:
    if player == 0:
        print("Você ganhou!!")
    elif player == 1:
        print("Deu Empate, jogue novamente")
    elif player == 2:
        print("Você perdeu, jogue novamente")
    else:
        print("Jogada Inválida!")
elif maquina == 2:
    if player == 0:
        print("Você perdeu, jogue novamente")
    elif player == 1:
        print("Você ganhou!!")
    elif player == 2:
        print("Deu Empate, jogue novamente")
    else:
        print("Jogada Inválida! ")
time.sleep(15)
