from time import sleep

print("=-=-" * 20)
print("Operador")
print("=-=-" * 20)

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
print("=-=-" * 20)
print("""Categorias Disponíveis """)
print("=-=-" * 20)
sleep(1.5)
maior = n1
opcao = 0
pao = 0
while pao != 5:
    print("""[1]Somar 
[2]Multiplicar
[3]maior
[4]novos números
[5]Sair do Programa""")
    opcao = int(input("Digite a Opção desejada: "))
    print("=-=-" * 20)
    if opcao == 1:
        soma = n1 + n2
        print(f"A opção desejada foi {opcao}, então o resultado é {soma}")
        print("=-=-" * 20)
    if opcao == 2:
        multi = n1 * n2
        print(f"A opção desejada foi {opcao}, então o resultado é {multi}")
        print("=-=-" * 20)
    if opcao == 3:
        if n1 > n2:
            print(f"O primeiro valor é {n1}, logo, ele é maior que o segundo que corresponde a {n2}")
        elif n1 < n2:
            print(f"O segundo valor é {n2}, logo, ele é maior que o primeiro que corresponde a {n1}!")
        elif n1 == n2:
            print("Os dois valores são iguais!!")
        print("=-=-" * 20)
    if opcao == 4:
        print("Informe os números novamente: ")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo Valor: "))
        print("=-=-" * 20)
    if opcao == 5:
        print("Finalizando...")
        print("Fim do Programa, Volte Sempre")
        print("=-=-" * 20)
        sleep(1)
        exit()
