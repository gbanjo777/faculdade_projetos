# Variáveis são usadas para salvar algo na memória do computador
# PEP8: Inicie variáveis com letras minúsculas, pode usar
#números e underline _.
#O sinal de = é o operador de atribuição. Ele é usado para atribuir um valor a um nome (variável).
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão
nome_completo = 'Luis Otávio Miranda'
soma_dois_mais_dois = 2 + 2
int_um = int('1')  # Converte string para inteiro
# SEMPRE descrever o que a variável representa, sem contradições.
#exemplo:
int_um = bool('1')  # Nesse caso, int_um não é um bom nome, pois a variável é do tipo bool (booleano)
print(int_um, type(int(int_um)))
print(nome_completo, soma_dois_mais_dois) # Luis Otávio Miranda 4
nome = 'Luis'
idade = 30
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
# Nome = string
# nome = Valor da string Nome
# Idade = string
# idade = Valor da string Idade
print('É maior de idade?', maior_de_idade)
