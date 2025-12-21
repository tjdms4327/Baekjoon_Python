import sys
input = sys.stdin.readline

t = int(input())
for case in range(1, 1+t):
    line = input().strip().split()
    n = int(line[0])
    A = list(map(int, line[1:]))
    
    result = [n-1] # 최고차항 차수 포함
    for a in A[:-1]:
        result.append(a*n)
        n -= 1
    print(f"Case {case}: {' '.join(map(str, result))}")
