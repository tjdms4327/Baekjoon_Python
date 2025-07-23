s=input().split()

srt=''
for i in s:
    if i==s[0]:
        srt+=i[0]
    else:
        if i not in ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']:
            srt+=i[0]
print(srt.upper())
        