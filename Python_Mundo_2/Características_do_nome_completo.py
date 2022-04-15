nome = str(input("Digite o seu nome completo: "))
maiuscula = nome.upper()
minuscula = nome.lower()
divi = nome.split()
qtd = len(nome) - nome.count(" ")
primeiro_nome = nome.find(" ")
print(f"""o nome em maiúscula é \033[1;35m{maiuscula}\033[m,
o nome em minúscula é \033[1;34m{minuscula}\033[m,
a quantidade de letras que tem o nome é \033[1;33m{qtd}\033[m,
a quantidade de letras que tem o primeiro nome da pessoa é \033[1;36m{primeiro_nome}\033[m""")