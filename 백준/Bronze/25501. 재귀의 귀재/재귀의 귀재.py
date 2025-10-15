# bronzeII_25501
import sys
input = sys.stdin.readline

def recursion(s, l, r):
    global count
    count += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: 
        recursion(s, l+1, r-1)

def isPalindrome(s):
    return s == s[::-1]


t = int(input())
for _ in range(t):
    s = input().strip()
    
    palindrome = isPalindrome(s)
    if palindrome:
        print(1, end=' ')
    else:
        print(0, end=' ')
    
    count = 0
    recursion(s, 0, len(s)-1)
    print(count)