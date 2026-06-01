"""
Método de Ordenamiento: Quick Sort (Ordenación Rápida)
======================================================
Algoritmo divide y vencerás. Elige un elemento "pivote"
y divide el arreglo en dos partes: menores al pivote y
mayores al pivote. Aplica el mismo proceso recursivamente
en cada parte.

Complejidad:
  - Mejor caso:    O(n log n)
  - Caso promedio: O(n log n)
  - Peor caso:     O(n²) → cuando el pivote es siempre el menor/mayor
  - Espacio:       O(log n) → por la pila de recursión
"""


def quick_sort(arr, inicio=0, fin=None):
    if fin is None:
        fin = len(arr) - 1

    if inicio < fin:
        indice_pivote = particionar(arr, inicio, fin)
        quick_sort(arr, inicio, indice_pivote - 1)   # Lado izquierdo
        quick_sort(arr, indice_pivote + 1, fin)       # Lado derecho
    return arr


def particionar(arr, inicio, fin):
    """Coloca el pivote en su posición correcta y reorganiza el arreglo."""
    pivote = arr[fin]   # Elegimos el último elemento como pivote
    i = inicio - 1      # Índice del elemento más pequeño

    for j in range(inicio, fin):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Colocar el pivote en su posición correcta
    arr[i + 1], arr[fin] = arr[fin], arr[i + 1]
    return i + 1


def mostrar_pasos(arr, nivel=0):
    if nivel == 0:
        print("=== Quick Sort ===")
        print(f"Lista original: {arr}")

    def _quick_sort_verbose(arr, inicio, fin, nivel):
        if inicio < fin:
            indice_pivote = particionar(arr, inicio, fin)
            sangria = "  " * (nivel + 1)
            print(f"{sangria}Pivote={arr[indice_pivote]}, partición → izq:{arr[inicio:indice_pivote]} | [{arr[indice_pivote]}] | der:{arr[indice_pivote+1:fin+1]}")
            _quick_sort_verbose(arr, inicio, indice_pivote - 1, nivel + 1)
            _quick_sort_verbose(arr, indice_pivote + 1, fin, nivel + 1)

    _quick_sort_verbose(arr, 0, len(arr) - 1, nivel)
    print(f"Lista ordenada: {arr}\n")
    return arr


if __name__ == "__main__":
    lista1 = [10, 7, 8, 9, 1, 5]
    mostrar_pasos(lista1)

    lista2 = [64, 34, 25, 12, 22, 11, 90]
    mostrar_pasos(lista2)

    lista3 = [1, 2, 3, 4, 5]
    mostrar_pasos(lista3)
