"""
Método de Ordenamiento: Comb Sort
==================================
Mejora del Bubble Sort. Al igual que Shell Sort mejora Insertion Sort,
Comb Sort mejora Bubble Sort usando un "gap" (intervalo) mayor a 1
que se va reduciendo con cada pasada hasta llegar a 1.

Esto elimina las "tortugas" (valores pequeños al final del arreglo)
que hacen lento al Bubble Sort clásico.

El factor de reducción estándar es 1.3 (determinado empíricamente).

Complejidad:
  - Mejor caso:    O(n log n)
  - Caso promedio: O(n² / 2^p)  donde p = número de incrementos
  - Peor caso:     O(n²)
  - Espacio:       O(1) → in-place
"""


def comb_sort(arr):
    n = len(arr)
    gap = n
    factor_reduccion = 1.3
    ordenado = False

    while not ordenado:
        # Reducir el gap
        gap = int(gap / factor_reduccion)
        if gap <= 1:
            gap = 1
            ordenado = True  # Asumimos que está ordenado; si hay intercambio, no lo está

        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                ordenado = False
            i += 1

    return arr


def mostrar_pasos(arr):
    print("=== Comb Sort ===")
    print(f"Lista original: {arr}")

    n = len(arr)
    gap = n
    factor_reduccion = 1.3
    ordenado = False
    paso = 1

    while not ordenado:
        gap = int(gap / factor_reduccion)
        if gap <= 1:
            gap = 1
            ordenado = True

        i = 0
        hubo_intercambio = False
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                ordenado = False
                hubo_intercambio = True
            i += 1

        print(f"  Paso {paso} (gap={gap}): {arr}{' ← intercambios' if hubo_intercambio else ''}")
        paso += 1

    print(f"Lista ordenada: {arr}\n")
    return arr


if __name__ == "__main__":
    lista1 = [64, 34, 25, 12, 22, 11, 90]
    mostrar_pasos(lista1)

    lista2 = [5, 4, 3, 2, 1]
    mostrar_pasos(lista2)

    lista3 = [8, 4, 1, 56, 3, -44, 23, -6, 28, 0]
    mostrar_pasos(lista3)
