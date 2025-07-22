n=int(input())
s=input()
t=input()

cnt_s, cnt_t=0,0
for i in range(n):
    if s[i]=='S' and t[i]=='P':
        cnt_s+=1
    elif (s[i]=='R' and t[i]=='P') or (s[i]=='S' and t[i]=='R'):
        cnt_t+=1
print(cnt_s, cnt_t)