from time import sleep

print("=-=-" * 25)
print("Programa de Empréstimo")
print("=-=-" * 25)
casa = float(input("Valor da Casa: "))
print("=-=-" * 25)
salario = float(input("Valor do Salario: "))
print("=-=-" * 25)
anos = int(input("Em quanto anos irá pagar: "))
print("=-=-" * 25)
soma = (anos * 12)
parcela = float(casa / soma)
aprovacao = float(salario * 0.3)
sleep(1.5)
if parcela > aprovacao:
    print("Você não conseguirá o empréstimo bancário.")
elif parcela < aprovacao:
    print("Você conseguirá o empréstimo bancário")
    print(f"Você terá que pagar durante {anos} anos, "
          f"o valor de R${parcela:.2f}")
sleep(20)
