# IA_P3 – Métodos de Ordenamiento

Implementaciones en Python de métodos de ordenamiento.

## Algoritmos implementados

| Archivo | Algoritmo | Tipo | Complejidad promedio |
|---|---|---|---|
| `bubble_sort.py` | Burbuja (BubbleSort) | Intercambio | O(n²) |
| `cocktail_sort.py` | Burbuja Bidireccional (CocktailSort) | Intercambio | O(n²) |
| `comb_sort.py` | Comb Sort | Intercambio (mejorado) | O(n²/2ᵖ) |
| `insertion_sort.py` | Inserción (InsertionSort) | Inserción | O(n²) |
| `shell_sort.py` | Shell Sort | Inserción (mejorado) | O(n log² n) |
| `selection_sort.py` | Selección (SelectionSort) | Selección | O(n²) |
| `enumeration_sort.py` | Enumeración | Enumeración | O(n²) |
| `heap_sort.py` | Heap Sort | Árbol | O(n log n) |
| `quick_sort.py` | Quick Sort | Divide y vencerás | O(n log n) |
| `merge_sort.py` | Merge Sort | Divide y vencerás | O(n log n) |
| `counting_sort.py` | Counting Sort | No comparativo | O(n + k) |
| `radix_sort.py` | Radix Sort | No comparativo | O(n·k) |
| `bucket_sort.py` | Bucket Sort | No comparativo | O(n + k) |

## ¿Cómo ejecutar?

```bash
python MetodosOrdenamiento/bubble_sort.py
python MetodosOrdenamiento/cocktail_sort.py
python MetodosOrdenamiento/comb_sort.py
python MetodosOrdenamiento/insertion_sort.py
python MetodosOrdenamiento/shell_sort.py
python MetodosOrdenamiento/selection_sort.py
python MetodosOrdenamiento/enumeration_sort.py
python MetodosOrdenamiento/heap_sort.py
python MetodosOrdenamiento/quick_sort.py
python MetodosOrdenamiento/merge_sort.py
python MetodosOrdenamiento/counting_sort.py
python MetodosOrdenamiento/radix_sort.py
python MetodosOrdenamiento/bucket_sort.py
```

Cada archivo muestra el proceso paso a paso en consola.

## Descripción de cada método

### Burbuja (BubbleSort) — Intercambio
Compara pares adyacentes e intercambia si están en orden incorrecto. Incluye optimización para detectar cuando ya está ordenado.

### Burbuja Bidireccional (CocktailSort) — Intercambio
Variante del Burbuja que recorre el arreglo en ambas direcciones, colocando el menor al inicio y el mayor al final en cada pasada.

### Comb Sort — Intercambio mejorado
Mejora del Burbuja usando un gap mayor a 1 que se reduce con factor 1.3. Elimina las "tortugas" (pequeños al final) que hacen lento al Burbuja.

### Inserción (InsertionSort) — Inserción
Toma cada elemento y lo inserta en su posición correcta respecto a los ya ordenados. Funciona como ordenar cartas en la mano.

### Shell Sort — Inserción mejorada
Extensión de Inserción. Compara elementos separados por un intervalo (gap) que va reduciéndose, logrando mejor rendimiento que Inserción pura.

### Selección (SelectionSort) — Selección
Busca el elemento mínimo del subarreglo restante y lo coloca en su posición. Realiza exactamente n-1 intercambios.

### Enumeración — Enumeración
Cada elemento se compara contra todos los demás y se cuenta cuántos son menores, determinando su posición final directamente.

### Heap Sort — Árbol binario
Construye un max-heap y extrae el máximo repetidamente. Garantiza O(n log n) en todos los casos y es in-place.

### Quick Sort — Divide y vencerás
Elige un pivote y divide el arreglo en dos partes (menores y mayores), aplicando el proceso recursivamente.

### Merge Sort — Divide y vencerás
Divide el arreglo en mitades hasta tener elementos individuales, luego los fusiona ordenadamente. Garantiza O(n log n) siempre.

### Counting Sort — No comparativo
Cuenta cuántas veces aparece cada valor y los coloca directamente en su posición. Ideal para enteros en rangos pequeños.

### Radix Sort — No comparativo
Ordena dígito por dígito usando Counting Sort como subrutina. No compara elementos directamente.

### Bucket Sort — No comparativo
Distribuye los elementos en cubetas por rango, ordena cada cubeta por separado y las concatena.
