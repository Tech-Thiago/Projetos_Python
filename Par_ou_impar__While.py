import random

print("=-=-" * 15)
titulo = "Vamos jogar PAR OU IMPAR"
print(titulo.center(55))
print("=-=-" * 15)
cont = 0
while True:
    n = int(input("Digite um valor: "))
    computador = random.randint(0, 10)
    vr = n + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou Impar? [P/I] ")).strip().upper()[0]
    print("=-=-" * 15)
    print(f"Você jogou {n} e o computador jogou {computador}, total de {vr}")
    print("=-=-" * 15)
    if tipo == "P":
        if vr % 2 == 0:
            print("Você ganhou, Parabêns")
            cont += 1
            print("=-=-" * 15)
        else:
            print("Você perdeu, Que pena")
            print("=-=-" * 15)
            break
    elif tipo == "I":
        if vr % 2 != 0:
            print("Você ganhou, Parabêns")
            cont += 1
            print("=-=-" * 15)
        else:
            print("Você perdeu, Que pena")
            print("=-=-" * 20)
            break
    print("Vamos jogar novamente...")
print(f"Você venceu {cont} partida")
print("=-=-" * 20)
