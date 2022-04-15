import random

j= str(input("Digite o nome do aluno 1: "))
k = str(input("Digite o nome do aluno 2: "))
l = str(input("Digite o nome do aluno 3: "))
m = str(input("Digite o nome do aluno 4: "))
lista = [j,k,l,m]
random.shuffle(lista)
print(f"O aluno escolhido foi \033[1;34m{lista}")