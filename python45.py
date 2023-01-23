""" 
Iterável ->str , range , etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
ite -> me entregue seu iterador
"""

texto = 'Bruno' # Iteravel
# iterador = iter(texto) #iterador

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)