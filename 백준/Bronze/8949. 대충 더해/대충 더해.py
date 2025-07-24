a, b=input().split()
max_len=max(len(a), len(b))

a='0'*(max_len-len(a))+a
b='0'*(max_len-len(b))+b

for i in range(max_len):
    print(int(a[i])+int(b[i]), end='')