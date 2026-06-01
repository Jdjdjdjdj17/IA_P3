"""
Método de Ordenamiento: Heap Sort (Ordenamiento de Árbol)
=========================================================
Usa una estructura de árbol binario especial llamada "heap"
(montículo). Primero construye un max-heap con todos los
elementos, luego extrae repetidamente el máximo y lo coloca
al final del arreglo.

Conceptos clave:
  - Max-Heap: el padre siempre es mayor que sus hijos
  - Para el nodo en índice i:
      * Hijo izquierdo: 2*i + 1
      * Hijo derecho:   2*i + 2
      * Padre:          (i-1) // 2

Complejidad:
  - Mejor caso:    O(n log n)
  - Caso promedio: O(n log n)
  - Peor caso:     O(n log n)
  - Espacio:       O(1) → in-place
"""


def heapify(arr, n, i):
    """
    Convierte el subárbol con raíz en índice i en un max-heap.
    n = tamaño del heap.
    """
    mayor = i          # Asumir que la raíz es el mayor
    izquierdo = 2 * i + 1
    derecho = 2 * i + 2

    # Verificar si el hijo izquierdo es mayor que la raíz
    if izquierdo < n and arr[izquierdo] > arr[mayor]:
        mayor = izquierdo

    # Verificar si el hijo derecho es mayor que el actual mayor
    if derecho < n and arr[derecho] > arr[mayor]:
        mayor = derecho

    # Si el mayor no es la raíz, intercambiar y continuar
    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        heapify(arr, n, mayor)


def heap_sort(arr):
    n = len(arr)

    # Fase 1: Construir el max-heap (de abajo hacia arriba)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Fase 2: Extraer elementos del heap uno por uno
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]   # Mover raíz (máximo) al final
        heapify(arr, i, 0)                 # Restaurar heap en el resto

    return arr


def mostrar_pasos(arr):
    print("=== Heap Sort ===")
    print(f"Lista original: {arr}")
    n = len(arr)

    # Construir max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    print(f"  Max-Heap construido: {arr}")

    # Extraer elementos
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
        print(f"  Extraer máximo → {arr}")

    print(f"Lista ordenada: {arr}\n")
    return arr


if __name__ == "__main__":
    lista1 = [12, 11, 13, 5, 6, 7]
    mostrar_pasos(lista1)

    lista2 = [64, 34, 25, 12, 22, 11, 90]
    mostrar_pasos(lista2)

    lista3 = [4, 10, 3, 5, 1]
    mostrar_pasos(lista3)
