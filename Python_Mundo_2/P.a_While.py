print("Gerador de PA")
print("=-=-" * 20)
primeiro = int(input("Digite o primeiro tempo: "))
razao = int(input("Digite a razão: "))
termo = primeiro
c = 1
while c <= 10:
    print(f"{termo}", end=" -> " if c != 10 else " --> ")
    termo += razao
    c += 1
print("Pausa")
