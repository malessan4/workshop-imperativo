# Uso de ambos mundos Imperativo y declarativo
numeros = [1,2,3,4,5,6,7,8,9]
def es_par(x):
    return x % 2 == 0

nueva_lista = [x * 3 for x in numeros if es_par(x)]
print (nueva_lista)

# Uso declarativo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nueva_lista = [x * 3 for x in numeros if x % 2 == 0]
print(nueva_lista)  # Output: [6, 12, 18, 24]