# bronzeII_9546
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    
    people = 0
    for _ in range(k):
        people += 0.5
        people *= 2
    print(int(people))