import sys
input = sys.stdin.readline

n = int(input())
D = list(map(int, input().split()))

for d in D: # 짝수 있을 경우
    if d!=2 and d % 2 == 0:
        print("YES")
        print(d)
        sys.exit()
        
for d in D:
    if d==0 or d==1:
        print('YES')
        print(d)
        sys.exit()
for i in range(n):
    for j in range(n):
        num = D[i] * 10 + D[j]
        if num > 3 and num%3==0:
            print('YES')
            print(num)
            sys.exit()
        for k in range(n):
            num = D[i] * 100 + D[j] * 10 + D[k]
            if num > 3 and num % 3 == 0:
                print("YES")
                print(num)
                sys.exit()
print('NO')