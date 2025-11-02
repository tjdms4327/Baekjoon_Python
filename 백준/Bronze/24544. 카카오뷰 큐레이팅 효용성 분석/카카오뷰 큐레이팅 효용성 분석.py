# bronzeII_24544
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
myView = list(map(int, input().split()))

print(sum(A))
print(sum(A[i] for i in range(n) if myView[i]==0))