numero = int(input("Digite um número: "))
print("""Escolha uma das opções abaixo para conversão:
 [ 1 ] Binário
 [ 2 ] Octal
 [ 3 ] Hexagonal """)
conversao = int(input("Digite o número da escolha: "))
binario = bin(numero)
octal = oct(numero)
hexagonal = hex(numero)
if conversao == 1:
    print(f"Sua opção foi o número 1 - Binário, aqui está o seu resultado {binario}")
elif conversao == 2:
    print(f"Sua opção foi o número 2 - octal, aqui está o seu resultado {octal}")
elif conversao == 3:
    print(f"Sua opção foi o número 3 - hexagonal, aqui está o seu resultado {hexagonal}")
else:
    print("Opção Inválida, Tente Novamente ")