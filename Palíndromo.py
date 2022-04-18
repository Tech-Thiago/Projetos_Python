frase = str(input("Digite uma frase: ")).upper()
divisao = frase.split()
juncao = "".join(divisao)
inversao = ""
for letra in range(len(juncao)-1, -1, -1):
    inversao += juncao[letra]
print(f"O inverso de {juncao} é {inversao}")
if inversao == juncao:
    print("Palíndromo")
else:
    print("Não é um Palíndromo")
