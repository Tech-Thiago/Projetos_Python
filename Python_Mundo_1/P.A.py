primeiro = int(input("Digite o primeiro tempo: "))
razao = int(input("Digite a razão: "))
for c in range(0, 10):
    print(f"{primeiro + razao * c}", end=" ")
print("Acabou")
