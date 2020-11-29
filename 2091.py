def heapify(elementos, n, i):
    raiz = i
    esq = 2 * i + 1
    dir = 2 * i + 2
    if esq < n and elementos[raiz] < elementos[esq]:
        raiz = esq
    if dir < n and elementos[raiz] < elementos[dir]:
        raiz = dir
    if raiz != i:
        elementos[i], elementos[raiz] = elementos[raiz], elementos[i]
        heapify(elementos, n, raiz)



def heapSort(elementos):
    n = len(elementos)

    for i in range(n // 2 - 1, -1, -1):
        heapify(elementos, n, i)

    for i in range(n - 1, 0, -1):
        elementos[i], elementos[0] = elementos[0], elementos[i]
        heapify(elementos, i, 0)


while True:
    n = int(input())
    if n == 0:
        break

    elementos = input().split()
    heapSort(elementos)

    aux = 0
    for i in range(0, len(elementos), 2):
        aux = i
        if i+1 >= len(elementos):
            break
        if int(elementos[i]) != int(elementos[i+1]):
            break

    print(elementos[aux])
