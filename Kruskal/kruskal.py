import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────
# Grafo de ejemplo (lista de aristas con pesos)
# ─────────────────────────────────────────────
aristas = [
    ("A", "B", 4),
    ("A", "C", 3),
    ("B", "C", 1),
    ("B", "D", 2),
    ("C", "E", 6),
    ("D", "E", 5),
    ("D", "F", 7),
    ("E", "F", 8),
    ("E", "G", 9),
    ("F", "G", 10),
]

nodos = sorted({u for u, v, _ in aristas} | {v for u, v, _ in aristas})

print("=" * 55)
print("  SIMULADOR: ÁRBOL DE MÍNIMO Y MÁXIMO COSTE — KRUSKAL")
print("=" * 55)
print("\nGrafo inicial (aristas y pesos):")
for u, v, w in aristas:
    print(f"  {u} ── {v}  (peso: {w})")


# ─────────────────────────────────────────────
# Union-Find (Conjuntos Disjuntos)
# ─────────────────────────────────────────────
class UnionFind:
    def __init__(self, nodos):
        self.padre = {n: n for n in nodos}
        self.rango  = {n: 0  for n in nodos}

    def find(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.find(self.padre[x])   # Compresión de camino
        return self.padre[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False        # Ya están en el mismo conjunto → ciclo
        if self.rango[rx] < self.rango[ry]:
            rx, ry = ry, rx
        self.padre[ry] = rx
        if self.rango[rx] == self.rango[ry]:
            self.rango[rx] += 1
        return True


# ─────────────────────────────────────────────
# Algoritmo de Kruskal (mínimo o máximo)
# ─────────────────────────────────────────────
def kruskal(aristas, nodos, modo="minimo"):
    """
    Construye el MST (mínimo) o MxST (máximo) usando Kruskal.
    modo: 'minimo' | 'maximo'
    """
    reverse = (modo == "maximo")
    aristas_ord = sorted(aristas, key=lambda e: e[2], reverse=reverse)

    print(f"\n{'─'*55}")
    print(f"  Modo: {'MÁXIMO COSTE' if reverse else 'MÍNIMO COSTE'}")
    print(f"  Aristas ordenadas por peso ({'desc' if reverse else 'asc'}):")
    for u, v, w in aristas_ord:
        print(f"    {u} ── {v}  (peso: {w})")

    uf = UnionFind(nodos)
    arbol = []
    costo  = 0
    paso   = 1

    print(f"\n  Construyendo el árbol paso a paso:")
    for u, v, w in aristas_ord:
        print(f"\n  [Paso {paso}] Evaluando arista {u} ── {v}  (peso: {w})")
        if uf.union(u, v):
            arbol.append((u, v, w))
            costo += w
            print(f"             ✔ Añadida al árbol. Costo acumulado: {costo}")
            print(f"             Árbol actual: {[(a,b,p) for a,b,p in arbol]}")
        else:
            print(f"             ✘ IGNORADA — formaría un ciclo.")
        paso += 1
        if len(arbol) == len(nodos) - 1:
            break

    return arbol, costo


# ─────────────────────────────────────────────
# Ejecutar ambos modos
# ─────────────────────────────────────────────
mst_min, costo_min = kruskal(aristas, nodos, modo="minimo")
print(f"\n{'=' * 55}")
print("  ÁRBOL DE MÍNIMO COSTE (MST) — RESULTADO")
print(f"{'=' * 55}")
for u, v, w in mst_min:
    print(f"  {u} ── {v}  (peso: {w})")
print(f"  Costo total: {costo_min}")

mst_max, costo_max = kruskal(aristas, nodos, modo="maximo")
print(f"\n{'=' * 55}")
print("  ÁRBOL DE MÁXIMO COSTE (MxST) — RESULTADO")
print(f"{'=' * 55}")
for u, v, w in mst_max:
    print(f"  {u} ── {v}  (peso: {w})")
print(f"  Costo total: {costo_max}")
print(f"{'=' * 55}\n")


# ─────────────────────────────────────────────
# Visualización gráfica (ambos árboles)
# ─────────────────────────────────────────────
def graficar_kruskal(aristas, mst_min, mst_max, nodos):
    G = nx.Graph()
    for u, v, w in aristas:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=7)
    edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges()}

    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    fig.suptitle("Algoritmo de Kruskal — Árboles de Mínimo y Máximo Coste", fontsize=14, fontweight="bold")

    for ax, arbol, titulo, color in [
        (axes[0], mst_min, f"Mínimo Coste  (total: {costo_min})", "#1F5C99"),
        (axes[1], mst_max, f"Máximo Coste  (total: {costo_max})", "#B85C00"),
    ]:
        arbol_edges = {(u, v) for u, v, _ in arbol} | {(v, u) for u, v, _ in arbol}
        normales = [(u, v) for u, v in G.edges() if (u, v) not in arbol_edges]
        destacadas = [(u, v) for u, v in G.edges() if (u, v) in arbol_edges]

        nx.draw_networkx_edges(G, pos, edgelist=normales, ax=ax,
                               edge_color="lightgray", width=1.5, style="dashed")
        nx.draw_networkx_edges(G, pos, edgelist=destacadas, ax=ax,
                               edge_color=color, width=3.5)
        nx.draw_networkx_nodes(G, pos, ax=ax, node_size=800,
                               node_color="lightyellow", linewidths=2, edgecolors=color)
        nx.draw_networkx_labels(G, pos, ax=ax, font_size=12, font_weight="bold")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax, font_size=8)
        ax.set_title(titulo, fontsize=12, color=color, fontweight="bold")
        ax.axis("off")

    plt.tight_layout()
    plt.savefig("grafo_kruskal.png", dpi=150)
    plt.show()
    print("  Gráfica guardada como 'grafo_kruskal.png'")


graficar_kruskal(aristas, mst_min, mst_max, nodos)
