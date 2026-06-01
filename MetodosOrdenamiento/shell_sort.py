"""
Método de Ordenamiento: Shell Sort
====================================
Extensión del método de Inserción. En lugar de comparar
elementos adyacentes, compara elementos separados por un
intervalo (gap) que va reduciéndose hasta llegar a 1.
Esto hace que los elementos se acerquen a su posición
correcta más rápido que Inserción pura.

Complejidad:
  - Mejor caso:    O(n log n)
  - Caso promedio: O(n log² n)
  - Peor caso:     O(n²)
  - Espacio:       O(1) → in-place
"""


def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Intervalo inicial: mitad del arreglo

    while gap > 0:
        # Inserción con el gap actual
        for i in range(gap, n):
            clave = arr[i]
            j = i
            while j >= gap and arr[j - gap] > clave:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = clave
        gap //= 2  # Reducir el intervalo a la mitad
    return arr


def mostrar_pasos(arr):
    print("=== Shell Sort ===")
    print(f"Lista original: {arr}")
    n = len(arr)
    gap = n // 2
    paso = 1

    while gap > 0:
        for i in range(gap, n):
            clave = arr[i]
            j = i
            while j >= gap and arr[j - gap] > clave:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = clave
        print(f"  Paso {paso} (gap={gap}): {arr}")
        paso += 1
        gap //= 2

    print(f"Lista ordenada: {arr}\n")
    return arr


if __name__ == "__main__":
    lista1 = [64, 34, 25, 12, 22, 11, 90]
    mostrar_pasos(lista1)

    lista2 = [5, 4, 3, 2, 1]
    mostrar_pasos(lista2)

    lista3 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    mostrar_pasos(lista3)
