"""
Método de Ordenamiento: Bucket Sort (Ordenamiento por Cubetas)
==============================================================
Divide los elementos en grupos llamados "cubetas" según su rango
de valor. Cada cubeta se ordena individualmente (con Insertion Sort
u otro método) y luego se concatenan todas en orden.

Muy eficiente cuando los datos están distribuidos uniformemente.

Complejidad:
  - Mejor caso:    O(n + k)  distribución uniforme
  - Caso promedio: O(n + k)
  - Peor caso:     O(n²)     todos los elementos en una sola cubeta
  - Espacio:       O(n + k)
"""


def insertion_sort_lista(lst):
    """Insertion Sort para ordenar cada cubeta."""
    for i in range(1, len(lst)):
        clave = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > clave:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = clave
    return lst


def bucket_sort(arr, num_cubetas=5):
    if not arr:
        return arr

    minimo = min(arr)
    maximo = max(arr)
    rango = maximo - minimo + 1

    # Crear cubetas vacías
    cubetas = [[] for _ in range(num_cubetas)]

    # Distribuir elementos en cubetas según su valor relativo
    for num in arr:
        indice = int((num - minimo) / rango * (num_cubetas - 1))
        cubetas[indice].append(num)

    # Ordenar cada cubeta y concatenar
    resultado = []
    for cubeta in cubetas:
        insertion_sort_lista(cubeta)
        resultado.extend(cubeta)

    return resultado


def mostrar_pasos(arr, num_cubetas=4):
    print("=== Bucket Sort ===")
    print(f"Lista original: {arr}")

    minimo = min(arr)
    maximo = max(arr)
    rango = maximo - minimo + 1

    cubetas = [[] for _ in range(num_cubetas)]
    for num in arr:
        indice = int((num - minimo) / rango * (num_cubetas - 1))
        cubetas[indice].append(num)

    print(f"  Distribución en {num_cubetas} cubetas:")
    for i, cubeta in enumerate(cubetas):
        print(f"    Cubeta {i}: {cubeta}")

    resultado = []
    for i, cubeta in enumerate(cubetas):
        insertion_sort_lista(cubeta)
        print(f"    Cubeta {i} ordenada: {cubeta}")
        resultado.extend(cubeta)

    print(f"Lista ordenada: {resultado}\n")
    return resultado


if __name__ == "__main__":
    lista1 = [64, 34, 25, 12, 22, 11, 90]
    mostrar_pasos(lista1)

    lista2 = [0.42, 0.32, 0.75, 0.11, 0.59, 0.27]
    mostrar_pasos(lista2, num_cubetas=3)

    lista3 = [5, 1, 4, 2, 8, 9, 3]
    mostrar_pasos(lista3)
