import time
import math
from typing import List
def f(n:int,a: List[float], x:float):
    p = a[n-1]
    for i in range(len(a)-1,0,-1):
        p = a[i-1] + x*p
    return p

def f2(n:int,a: List[float], x:float):
    p = a[0]
    for i in range(1,n):
        p = p + a[i]*math.pow(x,i)
    return p
    
MAXK = 10**6
a = [0]*101
a[0] = 1
for i in range(1,101):
    a[i] = 1./i
start_t = time.perf_counter()
for i in range(MAXK):
    ans = f2(101,a,1.1)
end_t = time.perf_counter()
print(ans,(end_t-start_t)/MAXK)