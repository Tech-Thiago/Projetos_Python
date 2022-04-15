n1 = float(input("\033[1;34mDigite sua primeira nota: "))
n2 = float(input("\033[1;34mDigite sua segunda nota\033[m: "))
media = (n1 + n2) / 2
if media < 5.0:
    print(f"""\033[1;35mSua nota foi {media}\033[m
\033[1;31mQUE PENA, VOCÊ FOI REPROVADO""")
elif (media > 5.0) and (media <= 6.9):
    print(f"""\033[1;35mSua nota foi {media}\033[m
\033[1;33mVOCÊ TERÁ QUE FAZER RECUPERAÇÃO""")
elif media > 7.0:
    print(f"""\033[1;35mSua nota foi {media}\033[m
\033[1;36mPARABÊNS, VOCÊ FOI APROVADO""")