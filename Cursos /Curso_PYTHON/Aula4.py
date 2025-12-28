# Tipos int e float
# int ->  Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado
# positivo.
print(11)        # int
print(-11)       # int
print(0)         # int
# float -> Número com ponto flutuante
# O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.
print(1.1, 10.11, -10.5)  # float
print(0.0, -0.0)          # float
# A função type mostra o tipo do dado
# A função type não é uma função, é uma classe
# Tudo que tem letra minúscula e tiver parenteses, se chama cálamo
print(type(11))     # <class 'int'>
print(type(-11))    # <class 'int'>
print(type(0))      # <class 'int'>
print(type(1.1))    # <class 'float'>
print(type('Otávio')) # <class 'str'>
print(type(0))  # <class 'str'>
print(type(1.1)), type(-1.1), type(0.0)  # <class 'float'>
#Tudo em python é um objeto