n=int(input())
spacejunks=list(map(int, input().split()))

min_spacejunk=min(spacejunks)
print(spacejunks.index(min_spacejunk))