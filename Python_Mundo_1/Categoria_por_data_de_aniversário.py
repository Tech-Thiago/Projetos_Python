from datetime import date
atual = date.today().year
nascimento = int(input("Qual é o ano do seu nascimento: "))
idade = atual - nascimento
if idade <= 9:
    print(f"Você tem {idade} anos, logo será da categoria \033[1;36mMIRIM\033[m ")
elif (idade > 9) and (idade <= 14):
    print(f"Você tem {idade} anos, logo será da categoria \033[1;36mINFANTIL\033[m")
elif (idade > 14) and (idade <= 19):
    print(f"Você tem {idade} anos, logo será da categoria \033[1;36mJUNIOR\033[m")
elif (idade > 19) and (idade <= 20):
    print(f"Você tem {idade} anos, logo será da categoria \033[1;36mSÊNIOR\033[m")
elif idade > 20:
    print(f"Você tem {idade} anos, logo será da categoria \033[1;36mMASTER\033[m")
