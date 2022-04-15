salario = float(input("Digite seu salário: "))
print(f"Seu salário antigo é \033[1;31m{salario}\033[m")
dinheiro = ((salario * 0.10) + salario)
if salario >= 1250:
    print(f"E passará a receber \033[1;36m{dinheiro}\033[m")
if salario < 1250:
    salario2 = ((salario * 0.15) + salario)
    print(f"E passará a receber \033[1;36m{salario2}\033[m")
