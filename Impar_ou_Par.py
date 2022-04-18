par_impar = float(input("Digite um número: "))
resultado = (par_impar % 2)
if resultado == 1:
    print("\033[1;31mSeu número é impar")
else:
    print("\033[1;36mSeu número é par")