# bronzeIII_30617
import sys
input = sys.stdin.readline

t = int(input())

L, R = [], []
fun = 0
for i in range(t):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
    
    if l != 0 and r != 0 and l == r:
        fun += 1
        
    if i == 0:
        continue
    if l != 0 and l == L[-2]:
        fun += 1
    if r != 0 and r == R[-2]:
        fun += 1
     
print(fun)