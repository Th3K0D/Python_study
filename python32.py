""" 
Faça um programa que peça ao usuáriopara digitar um número inteiro,
informe se este numero é par ou ímpar. Caso o usuário nao digite um número inteiro,
informe que não é um numero inteiro.
"""
######################################################################################################
#####                                           MANEIRA 1
######################################################################################################

# entrada = input("Digite um número inteiro: ")

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'impar'
    
#     if par_impar:
#         par_impar_texto = 'par'
#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print("Você nao digitou um numero inteiro!")

######################################################################################################
#####                                           MANEIRA 2
######################################################################################################

entrada = input("Digite um número inteiro: ")

try:
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'
    
    if par_impar:
        par_impar_texto = 'par'
    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print("Você nao digitou um numero inteiro!")




""" 
Faça um programa que pergunte a hora ao usuário e,
baseando-se no horário descrito, exiba a saudação apropriada. EX.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)
    
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa Tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Não conheço esta hora.')
except:
    print('Por favor! Digite um nímero inteiro.')
        

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver 5 e 6 letras, escreva "Seu nome é normal";
maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto!')
    
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal!')
    
    else:
        print('Seu nome é muito grande!')
else:
    print('Por favor! Digite ao menos 2 letra.')