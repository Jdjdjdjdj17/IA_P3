"""
Método de Ordenamiento: Inserción (InsertionSort)
=================================================
Toma cada elemento y lo inserta en su posición correcta
respecto a los elementos ya ordenados anteriormente.
Funciona igual que ordenar cartas en la mano.

Complejidad:
  - Mejor caso:    O(n)  → lista ya ordenada
  - Caso promedio: O(n²)
  - Peor caso:     O(n²)
  - Espacio:       O(1)  → in-place
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        clave = arr[i]       # Elemento actual a insertar
        j = i - 1
        # Desplazar a la derecha los elementos mayores que 'clave'
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave   # Insertar en la posición correcta
    return arr


def mostrar_pasos(arr):
    print("=== Inserción (InsertionSort) ===")
    print(f"Lista original: {arr}")
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
        print(f"  Paso {i}: insertar {clave} → {arr}")
    print(f"Lista ordenada: {arr}\n")
    return arr


if __name__ == "__main__":
    lista1 = [12, 11, 13, 5, 6]
    mostrar_pasos(lista1)

    lista2 = [9, 7, 5, 3, 1]
    mostrar_pasos(lista2)

    lista3 = [4, 2, 4, 1, 3, 2]
    mostrar_pasos(lista3)
