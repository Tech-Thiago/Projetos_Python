print("=-=-" * 20)
titulo = "Programa Tabuada"
print(titulo.center(75))
while True:
    print("=-=-" * 20)
    tabuada = int(input("Quer ver a tabuada de qual valor:"))
    print("=-=-" * 20)
    for c in range(0, 11):
        n = (tabuada * c)
        if tabuada >= 0:
            print(f"{tabuada} x {c} = {n}")
        if tabuada < 0:
            print("PROGRAMA ENCERRADO, Volte Sempre")
            exit()
