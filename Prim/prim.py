import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import heapq

# ─────────────────────────────────────────────
# Grafo de ejemplo (no dirigido, con pesos)
# ─────────────────────────────────────────────
grafo = {
    "A": {"B": 2, "D": 6},
    "B": {"A": 2, "C": 3, "D": 8, "E": 5},
    "C": {"B": 3, "E": 7},
    "D": {"A": 6, "B": 8, "E": 9, "F": 11},
    "E": {"B": 5, "C": 7, "D": 9, "F": 10, "G": 4},
    "F": {"D": 11, "E": 10, "G": 1},
    "G": {"E": 4, "F": 1},
}

print("=" * 55)
print("       SIMULADOR: ÁRBOL PARCIAL MÍNIMO — PRIM")
print("=" * 55)
print("\nGrafo inicial (aristas y pesos):")
for nodo, vecinos in grafo.items():
    for vecino, peso in vecinos.items():
        if nodo < vecino:           # Evitar duplicados en no dirigido
            print(f"  {nodo} ── {vecino}  (peso: {peso})")


# ─────────────────────────────────────────────
# Algoritmo de Prim
# ─────────────────────────────────────────────
def prim(grafo, inicio):
    """
    Construye el Árbol Parcial Mínimo (MST) usando el algoritmo de Prim.
    Retorna la lista de aristas del MST y su costo total.
    """
    visitados = {inicio}
    aristas_mst = []
    costo_total = 0

    # Cola de prioridad: (peso, nodo_origen, nodo_destino)
    cola = [(peso, inicio, vecino) for vecino, peso in grafo[inicio].items()]
    heapq.heapify(cola)

    print(f"\n{'─'*55}")
    print(f"  Nodo de inicio: {inicio}")
    print(f"  Visitados iniciales: {sorted(visitados)}")
    print(f"  Cola de prioridad inicial (peso, origen, destino):")
    for item in sorted(cola):
        print(f"    {item}")

    paso = 1
    while cola:
        peso, origen, destino = heapq.heappop(cola)

        if destino in visitados:
            print(f"\n  [Paso {paso}] Arista ({origen} → {destino}, peso={peso}) IGNORADA — {destino} ya visitado.")
            paso += 1
            continue

        # Agregar al MST
        visitados.add(destino)
        aristas_mst.append((origen, destino, peso))
        costo_total += peso

        print(f"\n  [Paso {paso}] Arista elegida: {origen} ──── {destino}  (peso: {peso})")
        print(f"             Visitados: {sorted(visitados)}")
        print(f"             Costo acumulado: {costo_total}")

        # Agregar vecinos del nuevo nodo a la cola
        nuevas = []
        for vecino, p in grafo[destino].items():
            if vecino not in visitados:
                heapq.heappush(cola, (p, destino, vecino))
                nuevas.append((p, destino, vecino))

        if nuevas:
            print(f"             Nuevas aristas añadidas a la cola: {nuevas}")

        paso += 1

    return aristas_mst, costo_total


# ─────────────────────────────────────────────
# Ejecutar Prim desde el nodo "A"
# ─────────────────────────────────────────────
inicio = "A"
mst, costo = prim(grafo, inicio)

print(f"\n{'=' * 55}")
print("  ÁRBOL PARCIAL MÍNIMO (MST) — RESULTADO FINAL")
print(f"{'=' * 55}")
for origen, destino, peso in mst:
    print(f"  {origen} ── {destino}  (peso: {peso})")
print(f"\n  Costo total del MST: {costo}")
print(f"{'=' * 55}\n")


# ─────────────────────────────────────────────
# Visualización gráfica
# ─────────────────────────────────────────────
def graficar_prim(grafo, mst):
    G_completo = nx.Graph()
    for nodo, vecinos in grafo.items():
        for vecino, peso in vecinos.items():
            G_completo.add_edge(nodo, vecino, weight=peso)

    mst_edges = {(u, v) for u, v, _ in mst} | {(v, u) for u, v, _ in mst}

    pos = nx.spring_layout(G_completo, seed=42)
    plt.figure(figsize=(10, 7))

    # Aristas normales (gris)
    aristas_normales = [(u, v) for u, v in G_completo.edges() if (u, v) not in mst_edges]
    nx.draw_networkx_edges(G_completo, pos, edgelist=aristas_normales,
                           edge_color="lightgray", width=1.5, style="dashed")

    # Aristas del MST (azul grueso)
    aristas_mst = [(u, v) for u, v in G_completo.edges() if (u, v) in mst_edges]
    nx.draw_networkx_edges(G_completo, pos, edgelist=aristas_mst,
                           edge_color="#1F5C99", width=3.5)

    # Nodos
    nx.draw_networkx_nodes(G_completo, pos, node_size=800,
                           node_color="lightblue", linewidths=2, edgecolors="#1F5C99")
    nx.draw_networkx_labels(G_completo, pos, font_size=12, font_weight="bold")

    # Pesos en aristas
    edge_labels = {(u, v): G_completo[u][v]['weight'] for u, v in G_completo.edges()}
    nx.draw_networkx_edge_labels(G_completo, pos, edge_labels=edge_labels, font_size=9)

    plt.title("Árbol Parcial Mínimo — Algoritmo de Prim\n(Aristas del MST en azul)", fontsize=13)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("grafo_prim.png", dpi=150)
    plt.show()
    print("  Gráfica guardada como 'grafo_prim.png'")


graficar_prim(grafo, mst)
