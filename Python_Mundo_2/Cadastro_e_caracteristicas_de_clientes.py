somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
idademulheres = 0

qtd = int(input("Quantas pessoas são: "))

for pessoas in range(1, qtd + 1):
    print(f"----------------------{pessoas}----------------------")
    nome = str(input("Digite seu nome: ")).strip()
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo (M/F): ")).strip()
    somaidade += idade
    if pessoas == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        idademulheres += 1
mediaidade = somaidade / qtd
print(f"A média da idade do grupo é de {mediaidade} anos ")
print(f"O homem mais velho é {nomevelho} com {maioridadehomem} anos")
print(f"{idademulheres} mulheres, essa é a quantidade de mulheres que tem menos de 20 anos")
