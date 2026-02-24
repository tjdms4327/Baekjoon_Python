import sys
input = sys.stdin.readline

c, m = [], []
for _ in range(3):
    c1, m1 = map(int, input().split())
    c.append(c1)
    m.append(m1)
    
for i in range(100):
    if m[i%3]+m[(i+1)%3] > c[(i+1)%3]: 
        diff = c[(i+1)%3] - m[(i+1)%3]
        m[(i+1)%3] = c[(i+1)%3]
        m[i%3] -= diff
    else:
        m[(i+1)%3] += m[i%3]
        m[i%3] = 0
    
print(*m, sep='\n')