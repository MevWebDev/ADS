import random
import math
from timeit import default_timer as timer
import sys
sys.setrecursionlimit(1000000)
def quickSort(A,low,high):
    if low<high :
        q = partition(A,low,high)
        quickSort(A,low,q)
        quickSort(A,q+1,high)
    return A

def partition(A,low,high):
    pivot=A[high] # element wyznaczajacy podział
    i=low-1
    for j in range (low, high+1):
        if A[j]<=pivot :
            i=i+1
            A[i], A[j] = A[j], A[i]
    if i<high :
        return i
    else:
        return i-1


def quickSort_test():
    rozmiary = [1000,5000,10000,50000]      
    for rozmiar in rozmiary:
        A = generateRandomArray(rozmiar)
        start = timer()
        quickSort(A,0,len(A)-1)
        stop = timer()
        Tn = stop-start
        print(rozmiar,Tn, "Random scenario")
        A = generateBadScenario(rozmiar)
        start = timer()
        quickSort(A,0,len(A)-1)
        stop = timer()
        Tn = stop-start
        print(rozmiar,Tn, "Bad scenario")





def generateRandomArray(n):
    A = []
    for i in range (n):
        A.append(random.randint(0,n))
    return A

def generateBadScenario(n):
    A = []
    for i in range(n):
        A.append(i)
    return A
quickSort_test()







