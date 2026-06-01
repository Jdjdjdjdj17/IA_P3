"""
Método de Ordenamiento: Enumeración (Enumeration Sort)
======================================================
Cada elemento es comparado contra todos los demás elementos
del arreglo. Se cuenta cuántos elementos son más pequeños
que el elemento analizado; ese conteo determina su posición
final en el arreglo ordenado.

Ejemplo: si hay 3 elementos menores que X, entonces X
va en la posición 3 (índice 3).

Complejidad:
  - Todos los casos: O(n²)
  - Espacio:         O(n) → necesita arreglo auxiliar para las posiciones
"""


def enumeration_sort(arr):
    n = len(arr)
    posicion = [0] * n   # Posición final de cada elemento

    # Para cada elemento, contar cuántos son menores que él
    for i in range(n):
        for j in range(n):
            if arr[j] < arr[i]:
                posicion[i] += 1
            # Desempate: si son iguales y j < i, i va después
            elif arr[j] == arr[i] and j < i:
                posicion[i] += 1

    # Colocar cada elemento en su posición correcta
    resultado = [0] * n
    for i in range(n):
        resultado[posicion[i]] = arr[i]

    return resultado


def mostrar_pasos(arr):
    print("=== Enumeración (Enumeration Sort) ===")
    print(f"Lista original: {arr}")
    n = len(arr)
    posicion = [0] * n

    for i in range(n):
        for j in range(n):
            if arr[j] < arr[i]:
                posicion[i] += 1
            elif arr[j] == arr[i] and j < i:
                posicion[i] += 1

    print(f"  Posiciones calculadas: {list(zip(arr, posicion))}")
    print(f"    (elemento, posición_final)")

    resultado = [0] * n
    for i in range(n):
        resultado[posicion[i]] = arr[i]

    print(f"Lista ordenada: {resultado}\n")
    return resultado


if __name__ == "__main__":
    lista1 = [64, 34, 25, 12, 22, 11, 90]
    mostrar_pasos(lista1)

    lista2 = [5, 3, 8, 1, 4]
    mostrar_pasos(lista2)

    lista3 = [4, 2, 4, 1, 3]
    mostrar_pasos(lista3)
