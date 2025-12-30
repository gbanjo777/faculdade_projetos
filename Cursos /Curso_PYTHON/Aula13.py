#printformatting f-strings
nome = 'Luiz Otávio'
altura = 203
peso = 80
imc = peso / (altura * altura)
print(f'{nome} tem {altura:,.2f} de altura,\n pesa {peso} quilos\n e seu IMC é de {imc}')