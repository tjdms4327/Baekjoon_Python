n, *a = map(int, open(0))

if not n:
    print(0)
    exit()
t = int(n * 0.15 + 0.5) # 15% 
m = int(sum(sorted(a)[t:n - t]) / (n - 2*t)   + 0.5)
print(m)