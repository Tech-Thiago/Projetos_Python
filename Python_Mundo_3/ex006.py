vogais = ("aáâã", "eéê", "iíî", "oóõô", "uúû")

palavras = ("Abduzir", "Adstrito", "Alarido", "Alcunha", "Belicoso",
            "Cominar", "Fugaz", "Crypts")

for p in palavras:
    print(f"\nNa palavra {p.upper()} temos ", end=" -> ")
    for letra in p:
        if letra in vogais:
            print(letra, end="")
