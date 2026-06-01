"""
Método de Ordenamiento: Counting Sort (Ordenamiento por Conteo)
===============================================================
No compara elementos entre sí. En cambio, cuenta cuántas veces
aparece cada valor y usa esos conteos para colocar cada elemento
directamente en su posición correcta.

Ideal para listas de enteros en un rango conocido y pequeño.

Complejidad:
  - Todos los casos: O(n + k)  donde k = rango de valores (max - min)
  - Espacio:         O(k)
"""


def counting_sort(arr):
    if not arr:
        return arr

    minimo = min(arr)
    maximo = max(arr)
    rango = maximo - minimo + 1

    # Contar ocurrencias de cada valor
    conteo = [0] * rango
    for num in arr:
        conteo[num - minimo] += 1

    # Reconstruir el arreglo ordenado
    resultado = []
    for i, freq in enumerate(conteo):
        resultado.extend([i + minimo] * freq)

    return resultado


def mostrar_pasos(arr):
    print("=== Counting Sort ===")
    print(f"Lista original: {arr}")

    minimo = min(arr)
    maximo = max(arr)
    rango = maximo - minimo + 1

    conteo = [0] * rango
    for num in arr:
        conteo[num - minimo] += 1

    print(f"  Rango: {minimo} a {maximo}")
    print(f"  Conteo por valor: { {i + minimo: conteo[i] for i in range(rango) if conteo[i] > 0} }")

    resultado = []
    for i, freq in enumerate(conteo):
        resultado.extend([i + minimo] * freq)

    print(f"Lista ordenada: {resultado}\n")
    return resultado


if __name__ == "__main__":
    lista1 = [4, 2, 2, 8, 3, 3, 1]
    mostrar_pasos(lista1)

    lista2 = [1, 4, 1, 2, 7, 5, 2]
    mostrar_pasos(lista2)

    lista3 = [10, 9, 8, 7, 6, 5]
    mostrar_pasos(lista3)
