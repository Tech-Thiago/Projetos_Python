repete = str(input("Digite uma frase: ")).upper().strip()
a = repete.count("A")
inicio = (repete.find("A")+1)
fim = (repete.rfind("A")+1)
print(f"""A letra a apareceu \033[1;34m{a}\033[m vezes, primeiramente na posição \033[1;35m{inicio}\033[m 
e por ultimo na posição e \033[1;36m{fim}'""")