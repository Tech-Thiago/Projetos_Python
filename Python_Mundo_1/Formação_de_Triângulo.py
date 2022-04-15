from time import sleep

print("\033[1;34m=-=-\033[m" * 15)
print("\033[1;35mANALISADOR DE TRIÂNGULOS\033[m")
print("\033[1;34m=-=-\033[m" * 15)
sleep(2.5)
a = float(input("\033[1;33mDigite o comprimento da reta 1: "))
b = float(input("\033[1;32mDigite o comprimento da reta 2: "))
c = float(input("\033[1;33mDigite o comprimento da reta 3: "))
print("\033[1;34m=-=-\033[m" * 15)
print("\033[1;35mANALISANDO...\033[m")
print("\033[1;34m=-=-\033[m" * 15)
sleep(4)
if a < b + c and b < a + c and c < a + b:
    print("\033[1;36mFormará um triângulo!\033[m")
else:
    print("\033[1;31mNão formará um triângulo!\033[m")
