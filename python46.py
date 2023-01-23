'''
i = coluna a = vai de 0 a 9  
j = coluna b =  vai de 1 a 2
 no continue , pode se colocar o break para encerrar apos o print
'''


for i in range(10):
    if i == 2:
        print(' i é 2 , pulando...')
        continue
    if i == 8:
        print(' i é 8, seu else não executará')
        continue
    for j in range(1 , 3):
        print(i, j)
else:
    print('For completo com sucesso!')