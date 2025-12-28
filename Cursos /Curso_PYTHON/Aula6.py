#Coersão de tipos, coerção
#type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos: str, int, float, bool
#print('1' + 1) # TypeError
print(int('1') + 1) # Coersão explícita
print(int('1'), type (int('1'))) # Coersão explícita
print(float('1') + 1) # Coersão explícita
print(str(11) + 'b') # Coersão explícita
# Coersão implícita
print(1 + 1.0) # O Python converteu o int 1 para float 1.0
print(type(1 + 1.0)) # float
print(bool(' ')) # O Python converteu a str ' ' para bool True
print(bool('')) # O Python converteu a str '' para bool False
print(True + 1) # O Python converteu o bool True para int 1
print(False + 1) # O Python converteu o bool False para int 0
print(type(True + 1)) # int
