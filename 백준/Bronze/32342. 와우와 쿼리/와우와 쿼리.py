n=int(input())
for _ in range(n):
    s=input()
    cnt=0
    for i in range(len(s)-2):
        if s[i:i+3]=='WOW':
            cnt+=1
    print(cnt)