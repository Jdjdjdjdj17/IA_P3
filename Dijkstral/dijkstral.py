import networkx as nx
import matplotlib.pyplot as plt

grafo = {
   "A": {"B": 3, "C": 3},
   "B": {"A": 3, "D": 3.5, "E": 2.8},
   "C": {"A": 3, "E": 2.8, "F": 3.5},
   "D": {"B": 3.5, "E": 3.1, "G": 10},
   "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
   "F": {"G": 2.5, "C": 3.5},
   "G": {"F": 2.5, "E": 7, "D": 10},
}

for key, value in grafo.items():
    for key2, value2 in value.items():
        print(f"{key} -> {key2}: {value2}")

def dijkstra(grafo, inicio, fin):
    ## Primero se inicializan las distancias de cada nodo a infinito, excepto el nodo de inicio que se inicializa a 0.
    distancia, nodo = {vertice: float('inf') for vertice in grafo}, inicio
    distancia[inicio] = 0

    print("\n\nPrimero se inicializan las distancias en infinito y el nodo de inicio en 0: ", distancia)

    camino = {vertice: None for vertice in grafo}
    visitados = [vertice for vertice in grafo]

    print("\n\nSe inicializa el diccionario de los nodos que se van eligiendo llamado caminos camino: ", camino)
    print("\nY se inicializa la lista de los nodos que se van a visitar llamada visitados: ", visitados)

    while visitados:
        nodo_mindist = min(visitados, key=lambda vertice: distancia[vertice])
        visitados.remove(nodo_mindist)

        print("\n\nSe elige el nodo con la distancia mínima: ", nodo_mindist)
        print("Y se elimina de la lista de visitados: ", visitados)

        if nodo_mindist != fin:
            print(f"\n\nLos vecinos de {nodo_mindist} son: {list(grafo[nodo_mindist].keys())}")

        for vecino in grafo[nodo_mindist]:

            if vecino in visitados:
                peso = grafo[nodo_mindist][vecino]
                costo = distancia[nodo_mindist] + peso
                print(f"\n\nSe evalúa el vecino {vecino} con peso {peso} y costo {costo}")

                if costo < distancia[vecino]:
                    distancia[vecino] = costo
                    camino[vecino] = nodo_mindist
                    print(f"Se elige el nodo {vecino} como el siguiente nodo con la distancia mínima: {distancia[vecino]} y se actualiza el camino: {list(camino.items())}")

    return distancia, camino


start = "A"
end = "G"
distancia, camino = dijkstra(grafo, start, end)
lista = []
actual = end
while actual in camino:
    lista.append(actual)
    actual = camino[actual]
    
lista = lista[::-1]
print("El camino es: ", lista, distancia[end])