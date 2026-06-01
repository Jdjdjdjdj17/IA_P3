"""
Método de Ordenamiento de la Burbuja Bidireccional (CocktailSort)
=================================================================
El Método de ordenamiento CocktailSort es una reforma del Método
de ordenamiento de la burbuja, con la diferencia que en este el
ordenamiento se realiza en ambas direcciones, comprobando que el
primero sin ordenar sea el menor y el último sin ordenar sea el
mayor, acomodando así en su respectivo lugar cada uno de los
elementos.

Complejidad:
  - Mejor caso:    O(n)   → lista ya ordenada
  - Caso promedio: O(n²)
  - Peor caso:     O(n²)
  - Espacio:       O(1)   → in-place
"""

from random import sample

# Importamos un Método de la biblioteca random para generar listas aleatorias

lista = list(range(100))  # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample
# (8 elementos aleatorios de la lista base)
vectorcocktail = sample(lista, 8)


def cocktailsort(vectorcocktail):
    """Esta función ordenara el vector que le pases como argumento
    con el Método de Cocktail Sort"""

    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con cocktail es:", vectorcocktail)

    largo = 0  # Establecemos un contador del largo

    for _ in vectorcocktail:
        largo += 1  # Obtenemos el largo del vector

    for i in range(largo // 2):  # Comenzamos desde la mitad aprox
        cambiar = False
        # Declaramos la variable que indica si es necesario intercambiar o no
        for j in range(1 + i, largo - i):
            # Probar si los dos elementos están en el orden incorrecto
            if vectorcocktail[j] < vectorcocktail[j - 1]:
                # Entonces ambos elementos cambian de lugar
                vectorcocktail[j], vectorcocktail[j - 1] = vectorcocktail[j - 1], vectorcocktail[j]
                cambiar = True
        # Si no ocurren cambios salimos del bucle
        if not cambiar:
            break
        cambiar = False
        for j in range(largo - i - 1, i, -1):
            # Probar si los dos elementos están en el orden incorrecto
            if vectorcocktail[j] < vectorcocktail[j - 1]:
                # Entonces ambos elementos cambian de lugar
                vectorcocktail[j], vectorcocktail[j - 1] = vectorcocktail[j - 1], vectorcocktail[j]
                cambiar = True
        if not cambiar:
            break
    print("El vector ordenado con cocktail es: ", vectorcocktail)


cocktailsort(vectorcocktail)
