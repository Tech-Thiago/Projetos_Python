cidade = str(input("Digite sua cidade: ")).strip()
popular = "SANTO" in cidade[:5].upper()
print(f"A cidade começa com o nome SANTO? \033[1:36m{popular}")
