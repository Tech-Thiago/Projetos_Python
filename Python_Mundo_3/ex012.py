exp = str(input("Digite a expressão: "))
lista = []
for simp in exp:
    if exp == "(":
        lista.append("(")
    elif simp == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")
            break
if len(lista) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está errada")
