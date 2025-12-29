#Precedência de operadores
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = (1 + (0.5 + 0.5)) ** (5 + 5)
# a conta sempre será executada da esquerda para a direita respeitando a precedência
print(conta_1)