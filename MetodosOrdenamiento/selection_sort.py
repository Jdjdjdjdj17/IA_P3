"""
Método de Ordenamiento: Selección (SelectionSort)
=================================================
Busca el elemento más pequeño del arreglo y lo coloca
en la primera posición. Luego repite con el resto,
avanzando una posición a la vez.

Complejidad:
  - Mejor caso:    O(n²)
  - Caso promedio: O(n²)
  - Peor caso:     O(n²)
  - Espacio:       O(1)  → in-place
"""


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Encontrar el índice del elemento mínimo en el subarreglo restante
        indice_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[indice_min]:
                indice_min = j
        # Intercambiar el mínimo encontrado con el primer elemento sin ordenar
        arr[i], arr[indice_min] = arr[indice_min], arr[i]
    return arr


def mostrar_pasos(arr):
    print("=== Selección (SelectionSort) ===")
    print(f"Lista original: {arr}")
    n = len(arr)
    for i in range(n):
        indice_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[indice_min]:
                indice_min = j
        arr[i], arr[indice_min] = arr[indice_min], arr[i]
        print(f"  Paso {i + 1}: mínimo={arr[i]}, colocado en pos {i} → {arr}")
    print(f"Lista ordenada: {arr}\n")
    return arr


if __name__ == "__main__":
    lista1 = [64, 25, 12, 22, 11]
    mostrar_pasos(lista1)

    lista2 = [5, 4, 3, 2, 1]
    mostrar_pasos(lista2)

    lista3 = [3, 1, 4, 1, 5, 9, 2, 6]
    mostrar_pasos(lista3)
