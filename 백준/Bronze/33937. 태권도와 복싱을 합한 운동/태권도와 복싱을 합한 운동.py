import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

def first(s):
    vowel = 'aeiou'
    
    ans = ''
    for x in s:
        
        if x not in vowel:
            if all(x not in vowel for x in ans):
                ans += x
            else:
                break
        else:
            ans += x
    
    if ans == s:
        return False
    
    return ans

sa = first(a)
sb = first(b)
if sa and sb:
    print(sa + sb)
else:
    print('no such exercise')