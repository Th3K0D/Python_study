# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4
# B r u n o
# -5-4-3-2-1

# nome = 'Bruno'
# print (nome[-1])

# print ('n' in nome)
# print ('w' in nome)


nome = input('Digite seu nome: ')
encontrar = input('Digite oque deseja encontrar: ')

if encontrar in nome:
    print (f'{encontrar} está em {nome}')
else:
    print (f'{encontrar} não está em {nome}')
