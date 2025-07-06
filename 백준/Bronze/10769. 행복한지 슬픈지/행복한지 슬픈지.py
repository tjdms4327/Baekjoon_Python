s=input()

h=s.count(':-)')
sa=s.count(':-(')
if h==0 and sa==0:
    print('none')
elif h==sa:
    print('unsure')
elif h>sa:
    print('happy')
else:
    print('sad')