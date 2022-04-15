import random
from time import sleep
vr = random.randint(0, 5)
print("\033[1;33m=-=-\033[m" * 15)
aleatorio = int(input("Digite um número de 0 a 5: Tente adivinhar... "))
print("\033[1;33m=-=-" * 15)
print("\033[1;35mProcessando\033[1;34m...\033[m")
sleep(2)
print("\033[1;33m=-=-" * 15)
if aleatorio == vr:
    print("\033[1;36mMeus Parabens, você acertou!! ")
else:
    print("\033[1;31mQue pena, você errou!! ")