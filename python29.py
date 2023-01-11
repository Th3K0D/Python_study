'''
Introdução ao try/ except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

input sempre retorna string !! então é necessario tratar o retorno para executar
'''
# numero = input('Vou dobrar o numero que você digitar: ')

# numero_float = float(numero)

# print(f'O dobro de {numero} é {numero_float * 2:.2f}')


numero_str = input(
    'Vou dobrar o numero que você digitar: '
    )

try:
    print('STR:' , numero_str)
    numero_float = float(numero_str) ## Verifica o Fail Fast
    print('Float:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('VOcê não digitou um caracter numerico!')
# if numero_str.isdigit():
#     numero_float = float(numero_str)

#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')

# else:
#     print('VOcê não digitou um caracter numerico!')

