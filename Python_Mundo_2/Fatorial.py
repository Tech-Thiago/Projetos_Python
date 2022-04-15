import math

n = int(input("Digite um numero pra calcular a fatorial: "))
c = n
fact = math.factorial(n)
print(f"Calculando {n}!")
while c > 0:
    print(f"{c}", end="")
    print(" x " if c > 1 else " = ", end="")
    c -= 1
print(f"{fact}")
