a = float(input("Digite um número: "))
b = float(input("Digite um número: "))
c = float(input("Digite um número: "))
menor = a
if b>a and b>c:
    menor = b
if c<a and c<b:
    menor = c
print(f"O menor valor digitado foi \033[1;36m{menor}")