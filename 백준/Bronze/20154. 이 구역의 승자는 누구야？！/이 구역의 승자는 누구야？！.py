# bronzeI_20154
import sys
input = sys.stdin.readline

strokes = [3, 2, 1, 2, 3, 3, 3, 3,
           1, 1, 3, 1, 3, 3, 1, 2,
           2, 2, 1, 2, 1, 1, 2, 2,
           2, 1]

s = input().strip()
lst = [strokes[ord(i) - ord('A')] for i in s]

while len(lst) > 1:
    last = None
    if len(lst) % 2 != 0:
        last = lst[-1]
        
    lst = [(lst[i]+lst[i+1])%10 for i in range(0,len(lst)-1, 2)]
    if last is not None:
        lst.append(last)

if lst[-1] % 2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")