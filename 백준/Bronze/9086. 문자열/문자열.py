T=int(input())

word=[]
for i in range(T):
    word.append(input())

for i in range(T):
    w=word[i]
    print(w[0]+w[-1])