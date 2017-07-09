

## Enigme "si ... alors ..."

def fonc(n):
    x = n
    for i in range(n):
      #print(i,x)
      if x%2==0:
        x = x-3    
      else:
        x = 2*x+2
    return x

n = 7
print(n,fonc(n))


for n in range(200):
  if fonc(n)==100:
    print(n,fonc(n))


## Enigme "binaire"

a = 108
b = 89
bin(a)
bin(b)
bin(a&b)
x = 127-(a&b)
bin(x)
ans = format(x, 'b').zfill(7)
int(ans,2)
Je pars de $a=551



## Enigme "couleurs"

R = 0xCE  # 206
V = 0xB6  # 182
B = 0x7D  # 125
G = 0.21*R+0.72*V+0.07*B
G
GG = hex(round(G))
GG

# Square root
import math

def mysqrt(n):
  oldrac = -1, rac = 1
  while abs(rac-oldrac) > 1:
    
    rac = (rac + n/rac) / 2
    oldrac = rac
  return int(round(rac))

# Test
N = 10000
print(mysqrt(N))
print(math.sqrt(N))



# Pair/impair

def myodd(n):
  while n >= 3:    
    n = n - 4
  if n==1 or n==3:
      print('est impair')   
  else:
      print('est pair')
    
  return None

myodd(2)
myodd(3)
myodd(4)
myodd(12)
myodd(13)


# Erreur nombres flottants

from math import *

# Calculer avec les flottants
# Tronquer
precision = 5                                # Nombre de décimales conserver
def tronquer(x):
    n = floor(log(x,10))                     # Exposant
    m = floor( x * 10 ** (precision-1 - n))  # Mantisse
    return m * 10 ** (-precision+1+n)        # Nombre tronquer
    
# Exemple
x = 1.23456789
print(x,"tronquer devient : ", tronquer(x))
x = 123.456789
print(x,"tronquer devient : ", tronquer(x))
x = 123456.789
print(x,"tronquer devient : ", tronquer(x))

a= 1286/9
b= 1000/7
x1 = tronquer(1/(a-b))
x2 = tronquer(1/tronquer((tronquer(a)-tronquer(b))))
x1
x2
print(x2-x1)


tronquer(x1-x2)


