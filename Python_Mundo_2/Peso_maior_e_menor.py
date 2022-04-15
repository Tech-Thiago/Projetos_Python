Peso = []
qtd = int(input("Informe quantas pessoas: "))

for c in range(0, qtd):
    Peso.append(int(input("Digite um número: ")))

print(f"O maior numero é: ", max(Peso))
print(f"O menor numero é: ", min(Peso))
