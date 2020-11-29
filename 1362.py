def calcula(p):
    global encontrado
    if p == int(m)+1:
        encontrado = True
        return
    if encontrado:
        return
    if quantidade[tipo[p][0]]:
        quantidade[tipo[p][0]] -= 1
        calcula(p + 1)
        quantidade[tipo[p][0]] += 1
    if quantidade[tipo[p][1]]:
        quantidade[tipo[p][1]] -= 1
        calcula(p + 1)
        quantidade[tipo[p][1]] += 1


def valor(tamanho):
    if tamanho == "XS":
        return 1
    if tamanho == "S":
        return 2
    if tamanho == "M":
        return 3
    if tamanho == "L":
        return 4
    if tamanho == "XL":
        return 5
    return 6


quantidade = [0] * 10
tipo = [[0 for i in range(2)] for j in range(40)]

casos = int(input())

for caso in range(casos):
    n, m = input().split()
    for i in range(10):
        quantidade[i] = int(n)/6;
    for i in range(1, int(m)+1):
        s1, s2 = input().split()
        tipo[i][0] = valor(s1)
        tipo[i][1] = valor(s2)

    encontrado = False
    calcula(1)

    if encontrado:
        print("YES")
    else:
        print("NO")
