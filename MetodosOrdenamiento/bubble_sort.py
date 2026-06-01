"""
Método de Ordenamiento: Burbuja (BubbleSort)
============================================
Compara pares de elementos adyacentes e intercambia si están
en el orden equivocado. Repite hasta que no haya intercambios.

Complejidad:
  - Mejor caso:    O(n)  → lista ya ordenada
  - Caso promedio: O(n²)
  - Peor caso:     O(n²)
  - Espacio:       O(1)  → in-place
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        intercambio = False  # Optimización: si no hay intercambios, ya está ordenado
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambio = True
        if not intercambio:
            break
    return arr


def mostrar_pasos(arr):
    print("=== Burbuja (BubbleSort) ===")
    print(f"Lista original: {arr}")
    n = len(arr)
    paso = 1
    for i in range(n):
        intercambio = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambio = True
        print(f"  Paso {paso}: {arr}")
        paso += 1
        if not intercambio:
            break
    print(f"Lista ordenada: {arr}\n")
    return arr


if __name__ == "__main__":
    lista1 = [64, 34, 25, 12, 22, 11, 90]
    mostrar_pasos(lista1)

    lista2 = [1, 2, 4, 3, 5]
    mostrar_pasos(lista2)

    lista3 = [9, 8, 7, 6, 5]
    mostrar_pasos(lista3)
