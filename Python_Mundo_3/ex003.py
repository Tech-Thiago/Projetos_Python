import random
n = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
     random.randint(1, 10), random.randint(1, 10))

print(f"Os numeros gerador são {n}")
print(f"O maior é {max(n)}")
print(f"O menor é {min(n)}")
