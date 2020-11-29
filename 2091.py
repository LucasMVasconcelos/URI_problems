
def hf(x, n, i):
    ml = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and x[ml] < x[l]:
        ml = l
    if r < n and x[ml] < x[r]:
        ml = r

    if ml != i:
        x[i], x[ml] = x[ml], x[i]
        hf(x, n, ml)

def HeapSort(x):
    n = len(x)
    for i in range(n//2 - 1, -1, -1):
        hf(x, n, i)

    for i in range(n-1, 0, -1):
        x[i], x[0] = x[0], x[i]
        hf(x, i, 0)

while True:
    n = int(input())
    if n!=0:
        x=[int(i) for i in input().split(" ")]
        heapSort(x)
        print(x[n-1])
    else:
        break
