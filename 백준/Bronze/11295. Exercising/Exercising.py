import sys
input = sys.stdin.readline

user = 0
while True:
    l = int(input())
    if l == 0: break
    
    user += 1
    print('User', user)
    n = int(input())
    for _ in range(n):
        num = int(input()) * l / 100 / 1000
        print(f'{num:.5f}')
    