lista = []
for n in range(0, 5):
    lista.append(int(input("Digite o número: ")))
print(f"\nOs números da lista são: {lista}"
      f"\nO valor máximo é {max(lista)}, na posição {lista.index(max(lista))+1}",
      f"\nO valor minímo é {min(lista)}, na posição {lista.index(min(lista))+1}")


