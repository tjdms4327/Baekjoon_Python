# bronzeIII_19963
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
m_set = set(map(int, input().split()))
k_set = set(map(int, input().split()))

get = m_set | k_set
print(n - len(get))
for i in range(1, n+1):
    if i not in get:
        print(i, end=' ')