# def heapify(A, heapSize, i):
#     l = 2*i+1 # lewy syn
#     r = 2*i+2 # prawy syn
#     if l < heapSize and A[l] > A[i]:
#         largest = l
#     else:
#         largest = i
#     if r < heapSize and A[r] > A[largest]:
#         largest = r
#     if largest != i:
#         A[i], A[largest] = A[largest], A[i]
#         heapify(A, heapSize, largest)
#     return A

def itHeapify(A, heapSize, i):
    while True:
        l = 2*i+1 # lewy syn
        r = 2*i+2 # prawy syn
        if l < heapSize and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r < heapSize and A[r] > A[largest]:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            i = largest
        else:
            break


def buildHeap(A):
    heapSize = len(A)
    k = int((len(A)-2)/2) # ojciec ostatniego węzła
    for i in range(k, -1, -1):
        itHeapify(A, heapSize, i)
    return A
def heapSort(A):
    A = buildHeap(A)
    heapSize = len(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[heapSize-1] = A[heapSize-1], A[0]
        heapSize -= 1
        itHeapify(A,heapSize,0)
    return A

with open('lab2/plik.txt', 'r') as file:
    list = [line.rstrip('\n') for line in file] 
print(list)
sortedList = heapSort(list)
print(sortedList)
with open('lab2/plik.txt', 'a') as file:
    file.write("\n")
    file.write("Sorted list\n")
    for i in sortedList:
        file.write(i +'\n')

