import random

vr = random.randint(0, 10)
print("Tente adivinhar o número de 0 a 10 ")
palpite = 0
acertou = False
aleatorio = int(input("Qual é o seu palpite: "))
while not acertou:
    aleatorio = int(input("Você errou, Tente Novamente: "))
    palpite += 1
    if vr == aleatorio:
        acertou = True
    else:
        if vr < aleatorio:
            print("Menos...")
        elif vr > aleatorio:
            print("Mais...")
print(f"Parabêns. Você acertou em {palpite} palpite")
