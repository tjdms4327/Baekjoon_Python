import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t+1):
    n = int(input())
    s = list(input().strip().split())

    print(f'Case {i}: This list contains {s.count("sheep")} sheep.\n')
