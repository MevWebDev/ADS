import math
import random
from timeit import default_timer as timer

def NAIWNY(n, M):
  maks=0
  lokalMaks=0
  for x1 in range (0,n):  
    for y1 in range (0,n):
      for x2 in range (n-1,x1-1,-1):
        for y2 in range (n-1,y1-1,-1):
          lokalMaks=0;
          for x in range (x1,x2+1):
            for y in range (y1,y2+1):  
              lokalMaks+=M[x][y]
          if lokalMaks==(x2-x1+1)*(y2-y1+1) and lokalMaks>maks:
              maks=lokalMaks
  return maks


def DYNAMICZNY(n,M):
  maks=0
  #  utworz tablicÄ kwadratowÄ MM rozmiaru n
  #  i wypeĹnij jÄ zerami
  MM = [[0 for _ in range(n)] for _ in range(n)]
  for y in range (0,n):
    for x1 in range (0,n):
      iloczyn=1
      for x2 in range (x1,n):
        iloczyn*=M[x2][y]
        MM[x1][x2]=iloczyn*(x2-x1+1+MM[x1][x2])
        if MM[x1][x2]>maks:
          maks=MM[x1][x2]                            
  return maks
                            

def CZULY(n, M):
  maks=0
  lokalMaks=0

  for x1 in range (0,n):  
    for y1 in range (0,n):
      lokalMaks=0
      x2=x1
      ymaks=n-1
      while (x2<n) and (M[x2][y1]==1):
            y2=y1;
            while (y2<ymaks+1) and (M[x2][y2]==1):
              y2+=1
            ymaks=y2-1
            lokalMaks=(x2-x1+1)*(ymaks-y1+1)
            if  lokalMaks>maks:
              maks=lokalMaks
            x2+=1
  return maks

# Test na tablicy rozmiaru 10. 
# Na pozycji [5][5] jest 0, reszta jedynki
n=10
M = [[1 for _ in range(n)] for _ in range(n)]
M[5][5]=0
print(M)
print(NAIWNY(n,M))
print(DYNAMICZNY(n,M))
print(CZULY(n,M))

def generujMacierze(n):
  macierz = []
  for i in range(n):
    wiersz = []
    for j in range(n):
      wiersz.append(random.randint(0, 0)) #tu zmienic zeby sprawdzic dla matrixu z samych 0 albo samych 1
    macierz.append(wiersz)
  return macierz


def pomiaryNaiwny():
    for n in [10, 20, 50]:
        print('Pomiar dla tablicy rozmiaru', n)
        M = generujMacierze(n)
        start = timer()
        NAIWNY(n,M)
        stop = timer()
        Fn = n*n*n*n*n*n
        Tn = stop - start
        print(n, Tn, Fn/Tn)
def pomiaryDynamiczny():
  for n in [10, 20, 50, 100, 200]:
    print('Pomiar dla tablicy rozmiaru', n)
    M = generujMacierze(n)
    start = timer()
    DYNAMICZNY(n,M)
    stop = timer()
    Fn = n*n*n
    Tn = stop - start
    print(n, Tn, Fn/Tn)

def pomiaryCzuly():
  for n in [10, 20, 50, 100, 200]:
    print('Pomiar dla tablicy rozmiaru', n)
    M = generujMacierze(n)
    start = timer()
    CZULY(n,M)
    stop = timer()
    Fn = n*n*n*n
    Tn = stop - start
    print(n, Tn, Fn/Tn)
print("------------Naiwny---------------")
pomiaryNaiwny()
print("------------Dynamiczny---------------")
pomiaryDynamiczny()
print("------------Czuly---------------")
pomiaryCzuly()

# ------------Naiwny---------------
# Pomiar dla tablicy rozmiaru 10
# 10 0.014395383999726619 69466712.38634488
# Pomiar dla tablicy rozmiaru 20
# 20 0.3301612960003695 193844647.3748043
# Pomiar dla tablicy rozmiaru 50
# 50 37.13412490299925 420771999.90077055

# ------------Dynamiczny---------------
# Pomiar dla tablicy rozmiaru 10
# 10 0.00024139199922501575 4142639.371687878
# Pomiar dla tablicy rozmiaru 20
# 20 0.0011784409998654155 6788630.063714386
# Pomiar dla tablicy rozmiaru 50
# 50 0.019249983999543474 6493511.89086518
# Pomiar dla tablicy rozmiaru 100
# 100 0.163651161999951 6110558.506149192
# Pomiar dla tablicy rozmiaru 200
# 200 1.2006365369998093 6663132.2248368915

# ------------Czuly---------------
# Pomiar dla tablicy rozmiaru 10
# 10 2.328100072190864e-05 429534800.47743297
# Pomiar dla tablicy rozmiaru 20
# 20 5.401899943535682e-05 2961920836.6024623
# Pomiar dla tablicy rozmiaru 50
# 50 0.00031339399993157713 19942947220.95686
# Pomiar dla tablicy rozmiaru 100
# 100 0.0022494599998026388 44455113675.62602
# Pomiar dla tablicy rozmiaru 200
# 200 0.0056953100001919665 280932907944.6194