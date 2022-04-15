n1 = float(input("Digite sua velocidade(km/h: "))
if n1 >= 80:
    print("\033[1;31m MULTADO, Você excedeu o limite permitido da via")
    multa = (n1 - 80) * 7
    print(f"\033[1;31mVocê será multado em {multa}")
else:
    print("\033[1;34mVocê não foi multado, Siga em frente! ")