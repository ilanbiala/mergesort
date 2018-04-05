import time, random

def merge(a, start1, start2, end):
    index1 = start1
    index2 = start2
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
    step = 1
    while (step < n):
        for start1 in range(0, n, 2*step):
            start2 = min(start1 + step, n)
            end = min(start1 + 2*step, n)
            merge(a, start1, start2, end)
        step *= 2

arr = [1, 3, 2, 4]
print(arr)
mergeSort(arr)
print(arr)

# builtinSort (wrapped as a function)
def builtinSort(a):
    a.sort()

# Generic testSort function
def testSort(sortFn, n):
    a = [random.randint(0,2**31) for i in range(n)]
    sortedA = sorted(a)
    sortFn(a)
    assert(a == sortedA)

def testSorts():
    n = 2**12
    for sortFn in [mergeSort, builtinSort]:
        testSort(sortFn, n)

testSorts()
