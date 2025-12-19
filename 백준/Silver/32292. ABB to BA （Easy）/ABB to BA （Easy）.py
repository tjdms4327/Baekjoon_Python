import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    
    while 'ABB' in s:
        s = s.replace('ABB', 'BA')
    print(s)