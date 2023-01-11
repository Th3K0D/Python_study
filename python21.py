# Operadore slógicos
# and (e) or (ou) not (não)
# and - todas as condições presisam ser verdadeiras.
# se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# são considerado falsy (que você já viu)
# 0 0 0  '' False
#Também existe o tipo de None que é usado para representar um não valor

# entrada = input("[E]ntrar [S]air ")
# senha_digitada = input("Senha: ")

# senha_permitida = '123456'

# if entrada == 'e' or 'E' and senha_digitada == senha_permitida:
#     print ('Entrar')
# else:
#     print ('Sair')

# avaliação de curto circuito 
print (True and False and True)
print (True and 0 and True)