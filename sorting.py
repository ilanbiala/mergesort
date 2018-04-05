import time, random

# iterative Mergesort implementation
# Takes 4 arguments: a, start1, start2, end
# a is an Array of comparable elements (usually ints)
# start1 is the left index to compare and merge from
# start2 is the left index to compare and merge from
# end is the end of the segment to be merged
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
            aux[i] = a[index1]
            index1 += 1
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
    startTime = time.time()
    sortFn(a)
    endTime = time.time()
    elapsedTime = endTime - startTime
    assert(a == sortedA)
    print("%20s n=%d  time=%6.3fs" % (sortFn.__name__, n, elapsedTime))

def testSorts():
    n = 2**12
    for sortFn in [mergeSort, builtinSort]:
        testSort(sortFn, n)

testSorts()
