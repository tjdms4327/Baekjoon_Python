import sys
input = sys.stdin.readline

n = int(input())

monitor = []
for i in range(1, n+1):
    w, h = map(int, input().split())
    ppi = w**2+h**2    
    monitor.append([ppi, i])

monitor.sort(key=lambda x: -x[0])
for _, idx in monitor:
    print(idx)