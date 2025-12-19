import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    me = input().strip()
    friend = input().strip()
    
    n = len(me)
    same = sum(1 for i in range(n) if me[i]==friend[i])
    diff = n - same
    
    answer = min(same, k) + min(diff, n - k)
    print(answer)