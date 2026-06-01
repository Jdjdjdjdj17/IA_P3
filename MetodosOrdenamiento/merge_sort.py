"""
Método de Ordenamiento: Merge Sort (Ordenamiento por Mezcla)
=============================================================
Algoritmo divide y vencerás. Divide el arreglo en mitades
recursivamente hasta tener subarreglos de 1 elemento (ya
ordenados), luego los fusiona (merge) de forma ordenada.

Complejidad:
  - Mejor caso:    O(n log n)
  - Caso promedio: O(n log n)
  - Peor caso:     O(n log n)
  - Espacio:       O(n) → necesita arreglo auxiliar
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Dividir el arreglo en dos mitades
    mid = len(arr) // 2
    izquierda = merge_sort(arr[:mid])
    derecha = merge_sort(arr[mid:])

    # Fusionar las dos mitades ordenadas
    return mezclar(izquierda, derecha)


def mezclar(izquierda, derecha):
    """Fusiona dos subarreglos ordenados en uno solo ordenado."""
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar los elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


def mostrar_pasos(arr):
    print("=== Merge Sort ===")
    print(f"Lista original: {arr}")

    def _merge_sort_verbose(arr, nivel):
        sangria = "  " * nivel
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        izquierda = arr[:mid]
        derecha = arr[mid:]
        print(f"{sangria}Dividir: {arr} → {izquierda} | {derecha}")
        izquierda = _merge_sort_verbose(izquierda, nivel + 1)
        derecha = _merge_sort_verbose(derecha, nivel + 1)
        mezclado = mezclar(izquierda, derecha)
        print(f"{sangria}Mezclar: {izquierda} + {derecha} → {mezclado}")
        return mezclado

    resultado = _merge_sort_verbose(arr, 0)
    print(f"Lista ordenada: {resultado}\n")
    return resultado


if __name__ == "__main__":
    lista1 = [38, 27, 43, 3, 9, 82, 10]
    mostrar_pasos(lista1)

    lista2 = [5, 4, 3, 2, 1]
    mostrar_pasos(lista2)

    lista3 = [1, 6, 3, 8, 2, 9, 4, 7]
    mostrar_pasos(lista3)
