import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    word = input().strip()
    len_word = len(word)
    
    best = float('inf')
    dic = {'upper':0, 'lower':0, 'num':0}
    left = 0
    for right in range(len_word):
        ch = word[right]
        if ch.isupper():
            dic['upper'] += 1
        elif ch.islower():
            dic['lower'] += 1
        elif ch.isdigit():
            dic['num'] += 1
        
        while dic['upper'] > 0 and dic['lower'] > 0 and dic['num'] > 0 and (right - left + 1) >= 6:
            best = min(best, right - left + 1)
    
            ch_left = word[left]
            if ch_left.isupper():
                dic['upper'] -= 1
            elif ch_left.islower():
                dic['lower'] -= 1
            elif ch_left.isdigit():
                dic['num'] -= 1
            left += 1
    
    print(0 if best == float('inf') else best)
