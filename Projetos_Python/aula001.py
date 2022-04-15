nome = str(input("Digite seu nome: "))
if nome == "Thiago":
    print("Que Nome Lindo!")
elif nome == "Pedro" or nome == "Maria" or nome =="Paulo":
    print("Seu nome é bem normal no Brasil")
elif nome in ("Gabriela Rubia João Helena"):
    print("Que nome Feminino Lindo!")
else:
    print("Seu nome é bem normal")
print(f"Tenha um belo dia, {nome}")