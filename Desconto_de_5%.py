num = int(input("Digite o preço do produto: "))
desconto = num - (num * 5 / 100)
print(f"O novo preço com desconto 5% será de \033[1;36m{desconto}")