from timeit import default_timer as timer
import math
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
nn = list(range(10, 1000, 10))
for n in nn:
    start = timer()
    NAIWNY(n,M)
    stop = timer()
    Tn = stop - start
    Fn = n * math.log(n, 2)
    print(f"n: {n}")
    print(f"Czas obliczeń: {Tn}")
    print(f"Stosunek Fn/Tn: {Fn/Tn}")

# Przykładowe użycie

