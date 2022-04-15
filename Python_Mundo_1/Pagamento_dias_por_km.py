dias = int(input("Quantos dias rodados? "))
km = int(input("Quantos km rodados? "))
s = (dias * 60) + (km * 0.15)
print(f"O total a pagar é de \033[1;36m{s}")