

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]


    def addRelation(self, v, w):
        v -= 1
        w -= 1
        self.adj[v].append(w)
        self.adj[w].append(v)

    def countUtil(self, v, visited):
        count = 1
        visited[v] = True
        i = 0
        while i != len(self.adj[v]):
            if (not visited[self.adj[v][i]]):
                count = count + self.countUtil(self.adj[v][i],
                                                      visited)
            i += 1
        return count

    def countGroups(self):


        visited = [0] * self.V
        n_people=[]
        existing_groups = 0
        new_groups = 1
        for i in range(self.V):

            # If not in any group.
            if (visited[i] == False):
                existing_groups += 1
                n_people.append(self.countUtil(i, visited))
                new_groups = (new_groups *
                              self.countUtil(i, visited))

        if (existing_groups == 1):
            new_groups = 0
        if (existing_groups == 1):
            existing_groups = -1


        return existing_groups,n_people



n = int(input())
houses = []
for _ in range(n):
    houses.append(input())
houses_target=[[1 if l=='S' else 0 for l in i] for i in houses]
g = Graph(n)
for linha in range(n):
    for coluna in range(n):
        if houses_target[linha][coluna]==1 and linha!=coluna:
            g.addRelation(linha, coluna)
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
