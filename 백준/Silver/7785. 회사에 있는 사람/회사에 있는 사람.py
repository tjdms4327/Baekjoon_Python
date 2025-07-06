incompany=set()

n=int(input())
for _ in range(n):
    name, record=input().split()
    if record=='enter':
        incompany.add(name)
    else:
        incompany.remove(name)
incompany=sorted(list(incompany), reverse=True)
print(*incompany, sep='\n')