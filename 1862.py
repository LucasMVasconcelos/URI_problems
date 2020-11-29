

class Grafo:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]


    def rel(self, v, w):
        v -= 1
        w -= 1
        self.adj[v].append(w)
        self.adj[w].append(v)

    def contaUtil(self, v, visitados):
        conta = 1
        visitados[v] = True
        i = 0
        while i != len(self.adj[v]):
            if (not visitados[self.adj[v][i]]):
                conta = conta + self.contaUtil(self.adj[v][i],
                                                      visitados)
            i += 1
        return conta

    def contaGrupos(self):


        visitados = [0] * self.V
        n_pessoas=[]
        e_grupos = 0
        grupos = 1
        for i in range(self.V):

            # If not in any group.
            if (visitados[i] == False):
                e_grupos += 1
                n_pessoas.append(self.contaUtil(i, visitados))
                grupos = (grupos *
                              self.contaUtil(i, visitados))

        if (e_grupos == 1):
            grupos = 0
        if (e_grupos == 1):
            e_grupos = -1


        return e_grupos,n_pessoas



n = int(input())
houses = []
for _ in range(n):
    houses.append(input())
houses_target=[[1 if l=='S' else 0 for l in i] for i in houses]
g = Grafo(n)
for linha in range(n):
    for coluna in range(n):
        if houses_target[linha][coluna]==1 and linha!=coluna:
            g.rel(linha, coluna)
n_groups,n_people_group=g.countGroups()
n_people_group.sort(reverse=True)
n_people_group_text=[str(i) for i in n_people_group]
text=" "
text=text.join(n_people_group_text)
print(n_groups)
if len(n_people_group_text)!=1:
    print(text)
else:
    pass
