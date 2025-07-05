w=[int(input()) for _ in range(10)]
w.sort()
k=[int(input()) for _ in range(10)]
k.sort()

print(sum(w[-3:]), sum(k[-3:]))