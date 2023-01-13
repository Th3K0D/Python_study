'''
repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> laço infinito de repetição do código
'''

qtd_linhas = 5
qtd_columns = 5

linha = 1

while linha <= qtd_linhas:
    column = 1

    while column <= qtd_columns:
        print(f'{linha=} {column=}')
        column += 1
    linha += 1
    
print('Acabou.')