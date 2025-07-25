n=int(input())
s=input()

num, low, up, special=False, False, False, False
for i in s:
    if i in '!@#$%^&*()-+':
        special=True
    elif i in '0123456789':
        num=True
    elif ord('a')<=ord(i)<=ord('z'):
        low=True
    elif ord('A')<=ord(i)<=ord('Z'):
        up=True
    if num==low==up==special==True:
        break
        
add=[num, low, up, special].count(0)
if add+n<6:
    add+=(6-n-add)
print(add)