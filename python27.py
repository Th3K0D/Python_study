'''
Fatiamento de string
012345678
Olá Mundo
-987654321
Fatiamento [inicio:fim:passo] [0:9:2] - neste caso ele inicia no zero e vai até o nove pulando 2 casas por vez
Obs.: a função len retorna a qtd de caracteres da str
obs2.: no fatiamento , se você colocar o passo negativo ele inverte a palavra
'''

# variavel = 'Olá Mundo!'
# print(len(variavel))

variavel = 'Olá Mundo'
print(variavel[0:9:2])