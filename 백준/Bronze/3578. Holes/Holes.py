def find_num(h):
    if h==0: return 1
    elif h==1: return 0
    elif h==2: return 8
    elif h%2==0: return '8'*(h//2)
    else: return '4'+'8'*(h//2)

h=int(input())
result=find_num(h)
print(result)