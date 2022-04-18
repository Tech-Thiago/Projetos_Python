import math

num = float(input("Digite o valor do cateto oposto: "))
nun = float(input("Digite o valor do cateto adjacente: "))
op = math.pow(num, 2) + math.pow(nun, 2)
raiz = math.sqrt(op)
print(f"A hipotenusa do triângulo retangulo será de \033[1;36m{raiz:.2f}")