# bronzeIII_14545
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l = int(input())
    print(l*(l+1)*(2*l+1)//6)