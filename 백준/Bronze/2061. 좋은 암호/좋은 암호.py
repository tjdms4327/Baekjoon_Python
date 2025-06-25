k,l=map(int, input().split())

def underl(k,l):
    for i in range(2,l):
        if k%i==0:
            return 'BAD '+str(i)
    return 'GOOD'

result=underl(k,l)
print(result)