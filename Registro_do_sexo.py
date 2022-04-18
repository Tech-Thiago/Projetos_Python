from time import sleep
print("=-=-" * 20)
print("""[M]Masculino [F]Feminino""")
sexo1 = str(input("Digite seu sexo: ")).upper().strip()
print("=-=-" * 20)
sleep(1)
while sexo1 not in "MmFf":
    print("""[M]Masculino [F]Feminino""")
    sexo1 = str(input("Dados inválidos. Informe seu sexo: "))
    print("=-=-" * 20)
    sleep(1)
sleep(1)
print(f"Sexo {sexo1}, registrado com sucesso!!")
