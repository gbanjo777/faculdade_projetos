nome = str(input('Digite seu nome: '))
sobrenome = str(input('Digite seu sobrenome: '))
idade = int(input('Digite sua idade: '))
ano_nascimento = int(input('Digite seu ano de nascimento: '))
maior_de_idade = idade >= 18
altura_metros = float(input('Digite sua altura em metros: '))
print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
#eu não consigo kkkk, preciso automatizar essa parte 
if maior_de_idade:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')
print('Altura em metros:', altura_metros)