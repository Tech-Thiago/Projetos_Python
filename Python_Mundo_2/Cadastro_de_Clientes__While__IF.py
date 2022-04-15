print("=-=-" * 15)
titulo = "Cadastro"
print(titulo.center(55))
print("=-=-" * 15)
i = p = s20 = 0
while True:
    idade = int(input("Qual é sua idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Qual seu sexo ? [M/F] ")).strip().upper()[0]
    if idade >= 18:
        i += 1
    if sexo == "M":
        p += 1
    if sexo == "F" and idade < 20:
        s20 += 1
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer Continuar ? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
print(f"""{i} pessoas com mais de 18 anos foram cadastradas
{p} pessoas são Homens
{s20} pessoas são mulheres que tem menos de 20 anos""")
