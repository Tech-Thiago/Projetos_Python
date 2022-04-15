listagem = ("arroz", 15, "Leite", 5, "Feijão", 10,
            "Macarrão", 4, "Papel higiênico", 20)


print("=-=" * 15)
print("Lista do Supermecado".center(45))
print("=-=" * 15)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end="")
    else:
        print(f"R$ {listagem[pos]:>7.2f}")
