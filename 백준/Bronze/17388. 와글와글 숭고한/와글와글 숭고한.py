s,k,h=map(int,input().split())

dic={}
dic[s]='Soongsil';dic[k]='Korea';dic[h]='Hanyang'

if s+k+h >=100:
    print('OK')
else: 
    d=min(s,k,h)
    print(dic[d])