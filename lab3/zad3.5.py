import random
import sys
from timeit import default_timer as timer
sys.setrecursionlimit(1000000)


def partition(A, p, r):
    pivot = random.randint(p, r)
    A[pivot], A[r] = A[r], A[pivot]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


def insertion_sort(A, p, r):
    for i in range(p+1, r+1):
        key = A[i]
        j = i-1
        while j >= p and key < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A


def quickSortB(A, p, r, c):
    
    if r - p + 1 < c:
        insertion_sort(A, p, r)
    elif p < r:
        
        q = partition(A, p, r)
        
        quickSortB(A, p, q - 1, c)
        quickSortB(A, q + 1, r, c)
    return A

def quickSort(A,p,r):
    if p<r :
        q = partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)
    return A
def generateRandomArray(n):
    A = []
    for i in range (n):
        A.append(random.randint(0,n))
    return A
def generateBadScenario(n):
    A = []
    for i in reversed(range(n)):
        A.append(i)
    return A

def quickSort_test():
    c = 15
    rozmiary = [1000,5000,10000,15000]      
    for rozmiar in rozmiary:
        
        A = generateRandomArray(rozmiar)
        print("-----Random numbers-----\n")
        start = timer()
        quickSort(A,0,len(A)-1)
        stop = timer()
        Tn = stop-start
        print("Quicksort zwykły", rozmiar, Tn)
        start = 0
        stop = 0
        start = timer()
        quickSortB(A,0,len(A)-1,c)
        stop = timer()
        Tn = stop-start
        print("Quicksort bąbelkowy", rozmiar, Tn,"\n")
        print("-----Bad scenario-----\n")
        A = generateBadScenario(rozmiar)
        start = 0
        stop = 0
        start = timer()
        quickSort(A,0,len(A)-1)
        stop = timer()
        Tn = stop-start
        print("Quicksort zwykły", rozmiar, Tn)
        start = 0
        stop = 0
        start = timer()
        quickSortB(A,0,len(A)-1,c)
        stop = timer()
        Tn = stop-start
        print("Quicksort bąbelkowy", rozmiar, Tn,"\n")
        

quickSort_test()