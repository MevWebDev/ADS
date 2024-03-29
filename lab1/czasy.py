import math
from timeit import default_timer as timer

def f1(n):
    s=0
    for j in range(1, n):
      s=s+1/j
    return s

def f2(n):
    s=0
    for j in range(1, n):
      for k in range(1, n):
        s=s+k/j
    return s

def f3(n):
    s=0
    for j in range(1, n):
      for k in range(j, n):
        s=s+k/j
    return s   
        
def f4(n):
    s=0
    for j in range(1, n):
      k=2
      while k<=n:
        s=s+k/j
        k=k*2
    return s           

def f5(n):
    s=0
    k=2
    while k<=n:
       s=s+1/k
       k=k*2
    return s   

nn = [2000, 4000, 8000, 16000, 32000]

# for n in nn:  
#   start = timer()
#   f1(n)
#   stop = timer()
#   Tn=stop-start
#   Fn=n
#   print(n, Tn, Fn/Tn)

# 2000 7.46800001252268e-05 26780931.931525305
# 4000 0.00014465899994320353 27651234.98413851
# 8000 0.00029007900002397946 27578694.077608783
# 16000 0.0005609670001831546 28522176.874532785
# 32000 0.0009114340000451193 35109508.75040418

# for n in nn:  
#   start = timer()
#   f2(n)
#   stop = timer()
#   Tn=stop-start
#   Fn=n*n
#   print(n, Tn, Fn/Tn)

# 2000 0.11818655800016131 33844796.46149387
# 4000 0.44558308300020144 35908005.95989585
# 8000 1.7951258840002993 35652095.80588351
# 16000 7.2405465870001535 35356446.77152252
# 32000 29.162363327000094 35113752.21952349


# for n in nn:  
#   start = timer()
#   f3(n)
#   stop = timer()
#   Tn=stop-start
#   Fn=n*n
#   print(n, Tn, Fn/Tn)

# 2000 0.05836330900001485 68536209.9671042
# 4000 0.2348425000000134 68130768.49377386
# 8000 0.9045270990000063 70755204.64865537
# 16000 3.7018591619998915 69154440.72747992
# 32000 14.774410393999915 69309026.39714544

# for n in nn:  
#   start = timer()
#   f4(n)
#   stop = timer()
#   Tn=stop-start
#   Fn=n*math.log(n,2)
#   print(n, Tn, Fn/Tn)

# 2000 0.0008351960000254621 18201481.949890465
# 4000 0.0018659890001799795 17779418.076531097
# 8000 0.004035597999973106 17815841.559485093
# 16000 0.008724233000066306 17753480.909825943
# 32000 0.018752217999917775 17701997.588683918

for n in nn:  
  start = timer()
  f5(n)
  stop = timer()
  Tn=stop-start
  Fn=math.log(n,2)
  print(n, Tn, Fn/Tn)

# 2000 0.0008201569999073399 26740695.46660209
# 4000 0.0018483510002624826 25895047.60289109
# 8000 0.003984717000093951 26031026.613646854
# 16000 0.008669392999763659 25774878.190512884
# 32000 0.018745072999990953 25548318.596007492

# inne funkcje czasu:

# Fn=math.log(n,2)
# Fn=n
# Fn=100*n
# Fn=n*math.log(n,2)
# Fn=n*n