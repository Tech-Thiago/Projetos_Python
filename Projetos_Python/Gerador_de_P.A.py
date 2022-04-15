print("Gerador de PA")
print("=-=-" * 20)
primeiro = int(input("Digite o primeiro tempo: "))
razao = int(input("Digite a razão: "))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f"{termo} -> ", end=" ")
        termo += razao
        c += 1
    print("Pausa")
    mais = int(input("Quantos termos voce quer mostrar a mais ? "))
print("Fim")
