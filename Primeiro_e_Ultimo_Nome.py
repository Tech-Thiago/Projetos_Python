nome = str(input("Digite seu nome completo: "))
inicio = nome.split()[0]
fim = nome.split()[-1]
print(f"""Seu nome é \033[1;35m{nome}\033[m,
seu primeiro nome é \033[1;34m{inicio}\033[m
e seu ultimo nome é \033[1;31m{fim}""")
