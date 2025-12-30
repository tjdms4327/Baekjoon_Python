import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

alice = bob = 0
for a in A:
    if n%2==0:
        alice += a
    else:
        bob += a
        
    if alice <= bob:
        print('Bob')
        sys.exit()

print('Alice')