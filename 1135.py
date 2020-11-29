from collections import defaultdict
from heapq import *

def dijkstra(adj, origem, destino):
    q, s, minimos = [(0, origem)], set(), {origem: 0}
    while q:
        (dist_u, u) = heappop(q)
        if u not in s:
            s.add(u)
            if u == destino: return (dist_u)

            for aresta, v in adj.get(u, ()):
                if v in s: continue
                caminho = minimos.get(v, None)
                dist_v = dist_u + aresta
                if caminho is None or dist_v < caminho:
                    minimos[v] = dist_v
                    heappush(q, (dist_v, v))


if __name__ == "__main__":
    while True:
        n_formigueiros = int(input())
        vertices = []

        if n_formigueiros == 0:
            break

        adj = defaultdict(list)
        for formigueiro in range(1, n_formigueiros):
            (tunel, caminho) = [int(i) for i in input().split(' ')]
            adj[formigueiro].append((caminho, tunel))
            adj[tunel].append((caminho, formigueiro))

        resultado = ""
        casos_teste = int(input())
        for caso in range(casos_teste):
            (origem, destino) = [int(i) for i in input().split(' ')]
            resultado = resultado + str(dijkstra(adj, origem, destino)) + " "
        print(resultado.strip())
