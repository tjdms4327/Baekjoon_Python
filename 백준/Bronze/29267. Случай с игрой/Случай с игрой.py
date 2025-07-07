def bullet_change(n, k, list_b):
    saving=0
    for _ in range(n):
        s=input()
        if s=='ammo':
            list_b.append(list_b[-1]+k)
        elif s=='shoot':
            if list_b[-1]>=1:
                list_b.append(list_b[-1]-1)
            else:
                list_b.append(0)
        elif s=='load':
            list_b.append(saving)
        elif s=='save':
            saving=list_b[-1]
            list_b.append(saving)
        print(list_b[-1])

n,k=map(int, input().split())
b=0
list_b=[0]
results=bullet_change(n,k,list_b)