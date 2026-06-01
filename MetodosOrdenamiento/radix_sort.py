"""
Método de Ordenamiento: Radix Sort
====================================
Ordena los elementos dígito por dígito, desde el dígito
menos significativo (unidades) hasta el más significativo.
No realiza comparaciones directas entre elementos; en cambio,
los agrupa en "cubetas" según el valor de cada dígito.

Usa Counting Sort internamente como subrutina estable.

Complejidad:
  - Todos los casos: O(n * k)  donde k = número de dígitos
  - Espacio:         O(n + b)  donde b = base (10 para decimal)
"""


def counting_sort_por_digito(arr, exp):
    """
    Counting Sort estable para ordenar por el dígito
    representado por 'exp' (1 → unidades, 10 → decenas, etc.)
    """
    n = len(arr)
    salida = [0] * n
    conteo = [0] * 10  # Dígitos del 0 al 9

    # Contar ocurrencias del dígito actual
    for i in range(n):
        digito = (arr[i] // exp) % 10
        conteo[digito] += 1

    # Acumular conteos (posición final de cada dígito)
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # Construir el arreglo de salida (recorrer de derecha a izquierda para estabilidad)
    for i in range(n - 1, -1, -1):
        digito = (arr[i] // exp) % 10
        salida[conteo[digito] - 1] = arr[i]
        conteo[digito] -= 1

    # Copiar resultado al arreglo original
    for i in range(n):
        arr[i] = salida[i]


def radix_sort(arr):
    if not arr:
        return arr

    maximo = max(arr)   # Encontrar el valor máximo para saber cuántos dígitos hay

    # Aplicar counting sort para cada posición de dígito
    exp = 1
    while maximo // exp > 0:
        counting_sort_por_digito(arr, exp)
        exp *= 10

    return arr


def mostrar_pasos(arr):
    print("=== Radix Sort ===")
    print(f"Lista original: {arr}")

    if not arr:
        return arr

    maximo = max(arr)
    exp = 1
    paso = 1

    while maximo // exp > 0:
        counting_sort_por_digito(arr, exp)
        nombre_digito = {1: "unidades", 10: "decenas", 100: "centenas"}.get(exp, f"exp={exp}")
        print(f"  Paso {paso} ({nombre_digito}): {arr}")
        exp *= 10
        paso += 1

    print(f"Lista ordenada: {arr}\n")
    return arr


if __name__ == "__main__":
    lista1 = [170, 45, 75, 90, 802, 24, 2, 66]
    mostrar_pasos(lista1)

    lista2 = [3, 6, 8, 10, 1, 2, 1]
    mostrar_pasos(lista2)

    lista3 = [64, 34, 25, 12, 22, 11, 90]
    mostrar_pasos(lista3)
