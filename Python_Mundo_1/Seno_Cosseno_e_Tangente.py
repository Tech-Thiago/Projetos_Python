import math

num = int(input("Digite um valor do angulo: "))
ip = math.sin(num)
op = math.cos(num)
up = math.tan(num)
print(f"Os valores do seno, cosseno e tangente são \033[1;33m{ip:.2f}, \033[1;36m{op:.2f}, \033[1:34m{up:.2f}")