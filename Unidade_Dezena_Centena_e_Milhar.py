digito = int(input("Digite um número com 4 digitos: "))
u = digito // 1 % 10
d = digito // 10 % 10
c = digito // 100 % 10
m = digito // 1000 % 10
print(f"""Unidade = \033[1;33m{u}\033[m,
dezena = \033[1;34m{d}\033[m,
centena = \033[1;36m{c}\033[m,
milhar = \033[1:32m{m}\033[m""")