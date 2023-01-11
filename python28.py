'''
Exercicio
peça ao usuário para digitar seu nome
peça para o usuario digitar sua idade
Se nome e idade forem digitados:
    exiba:
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    seu nome contem ( ou não) espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    a ultima letra do seu nome é {letra}
    se nada for difitado em nome ou idade:
    exiba:
    "Desculpe, você deixou campos vazios"
'''

# nome = input('Digite seu nome: ')
# idade = input('Digie sua idade: ')
# num_letras = len(nome)

# if nome != '':
#     print(f'Seu nome é {nome}') 
#     print(f'Seu nome invertido é {nome[::-1]}') # arrumar
#     print(f'Seu nome contem ( ou não) espaços')
#     print(f'Seu nome tem {len(nome)} letras')
#     print(f'A primeira letra do seu nome é {nome[0]}')
#     print(f'A ultima letra do seu nome é {nome[num_letras]}')
# elif nome or idade == '':
#     print('Desculpe, você deixou campos vazios.')

nome = input('Digite seu nome: ')
idade = input('Digie sua idade: ')


if nome and idade:
    print(f'Seu nome é {nome}') 
    print(f'Seu nome invertido é {nome[::-1]}')
    
    if ' ' in nome:
         print(f'Seu nome contem espaços')
    else:
        print(f'Seu nome não contem espaços')
        
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')