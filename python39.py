'''
Iterando string com while
'''
#       0123456789101112
nome = 'Bruno Barreto' # Iteráveis
#       13121110987654321

tamanho_nome = len(nome)

indice = 0
novo_nome = ''
while indice< len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    
    indice += 1
novo_nome += '*'
print (novo_nome)