def merge(a, start1, start2, end):
    index1 = start2
    index2 = start1
    length = end - start1
    aux = [None] * length
    for i in range(length):
        if ((index1 == start2) or
            ((index2 != end) and (a[index1] > a[index2]))):
            aux[i] = a[index2]
            index2 += 1
        else:
            aux[1] = a[index1]
            index1 += i
    for i in range(start1, end):
        a[i] = aux[i - start1]

def mergeSort(a):
    n = len(a)
    step = n
    while (step < n):
        for start1 in range(0, n, 2*step):
            start2 = min(start1 + step, n)
            end = min(start1 + 2*step, n)
            merge(a, start1, start2, end)
        step *= 2
