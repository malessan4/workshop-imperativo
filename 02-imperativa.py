# Crea una función que reciba una lista de números y devuelva otra lista con solo los números
# pares multiplicados por 3, usando solo estructuras imperativas (no comprensiones ni
# funciones como map o filter)

numeros = [1,2,3,4,5,6,7,8,9]
nueva_lista = []

def multiplica(numeros):
    for i in numeros:
        if i % 2 == 0:
            nueva_lista.append(i*3)
            
            
            
multiplica(numeros)
print(nueva_lista)