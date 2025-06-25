h=set()
s=set()

n,m=map(int, input().split())
for _ in range(n):
    h.add(input())
for _ in range(m):
    s.add(input())

hs=sorted(list(h.intersection(s)))
print(len(hs))
print(*hs, sep='\n')
