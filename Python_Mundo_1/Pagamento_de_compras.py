import time

produto = float(input("Preço do Produto: "))
print("""Digite a opção de pagamento
[1] À vista / Cheque: 10% de Desconto
[2] À vista no Cartão: 5% de Desconto
[3] Em até 2x no Cartão: preço normal
[4] 3x no Cartão: 20% de juros """)
print("=-=-" *  25)
pagamento = float(input("Opção Selecionada: "))
print("=-=-" *  25)
n1 = produto - (produto * 0.1)
n2 = produto - (produto * 0.05)
n3 = produto
n4 = produto + (produto * 0.2)
time.sleep(1)
if pagamento == 1:
    print(f"O valor do produto é {produto} e passará a ser R${n1}")
elif pagamento == 2:
    print(f"O valor do produto é {produto} e passará a ser R${n2}")
elif pagamento == 3:
    print(f"O valor do produto é {produto}. ", end="")
    parcela2x = (n3 / 2)
    print(f"As parcelas serão no valor de R${parcela2x}")
elif pagamento == 4:
    print(f"O valor do produto é {produto} e passará a ser R${n4}. ", end="")
    parcela3x = (n4 / 3)
    print(f"As parcelas serão no valor de R${parcela3x}")
else:
    print("\033[1;31mOpção Inválida. Tente Novamente\033[m")
