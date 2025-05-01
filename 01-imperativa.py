# Código con errores para corregir
# Código con mal uso del bucle y sin claridad

"""
nums = [1,2,3,4]
for i in nums:
    if i % 2 ==0:
        i = i * 2
    print(i)
"""

#Corregir para que solo los pares se dupliquen y la salida sea una nueva lista
# Version corregida

numeros = [1,2,3,4]
nueva_lista = []
for i in numeros:
    if i % 2 ==0:
        nueva_lista.append(i * 2)
        
print(nueva_lista)