import sys
input=sys.stdin.readline

n,k=map(float, input().split())
s=list(input().strip())

a, b, c='','',''
for i in s:
    if i=='s': # 파란색
        if len(a) < k:
            a+=i
        elif len(b) < k:
            b+=i
        else:
            c+=i
    elif i == 'r':  # 초록색
        if len(b) < k:
            b+=i
        elif len(c) < k:
            c+=i
        else:
            a+=i

    else:  # i == 'p' (빨간색)
        if len(c) < k:
            c+=i
        elif len(a) < k:
            a+=i
        else:
            b+=i

print(a)
print(b)
print(c)