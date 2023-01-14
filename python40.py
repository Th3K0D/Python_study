'''  Calculadora com while  '''

while True:
    primeiro_numero = input('Digite o primeiro numero: ')
    segundo_numero = input('Digite o segundo numero: ')
    operador = input('Digite o operador (+-/*): ')
    
    numero_validos = None
    
    try:
        primeiro_numero_float = float(primeiro_numero)
        segundo_numero_float = float(segundo_numero)
        numero_validos = True
    except:
        numero_validos = None
        
    if numero_validos is None:
        print('Foi identificado um caracter invalido!')
        continue
    
    operadores_permitido = '+-/*'
    
    if operador not in operadores_permitido:
        print('Operador invalido!')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue
    ###################################################################
    print('Realizando seu calculo! Confira abaixo: ')
    if operador == '+':
        print(f'{primeiro_numero_float} + {segundo_numero_float} =', primeiro_numero_float + segundo_numero_float)
    elif operador == '-':
        print(f'{primeiro_numero_float} - {segundo_numero_float} =', primeiro_numero_float - segundo_numero_float)
    elif operador == '/':
        print(f'{primeiro_numero_float} / {segundo_numero_float} =', primeiro_numero_float / segundo_numero_float)
    elif operador == '*':
        print(f'{primeiro_numero_float} * {segundo_numero_float} =', primeiro_numero_float * segundo_numero_float)
    else:
        print('Alerta de buraco negro! Se chegou até aqui o código esta errado!')
    
    ###################################################################
    sair = input('Quer [s]air?: ').lower().startswith('s')
   
    if sair is True:
       break
