number=[int(input()) for _ in range(4)]

if number[0] in [8,9] and number[-1] in [8,9] and number[1]==number[2]:
    print('ignore')
else:
    print('answer')