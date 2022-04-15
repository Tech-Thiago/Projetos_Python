from time import sleep

print("\033[1;34m=-=-\033[m" * 15)
data = float(input("\033[1;35mDigite o ano:\033[m "))
print("\033[1;34m=-=-\033[m" * 15)
bissex = (data % 4)
print("\033[1;33mPROCESSANDO...\033[m")
print("\033[1;34m=-=-\033[m" * 15)
sleep(3.5)
if bissex == 0:
    print("\033[1;36mEsse ano é bissexto\033[m")
else:
    print("\033[1;31mEsse ano não é bissexto\033[m")
print("\033[1;34m=-=\033[m" * 15)