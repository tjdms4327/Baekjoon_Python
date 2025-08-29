import sys
input = sys.stdin.readline

mapping = {'y':'a', 'a':'e', 'e':'i', 
           'i':'o', 'o':'u', 'u':'y',
           'Y':'A', 'A':'E', 'E':'I',
           'I':'O', 'O':'U', 'U':'Y'}

n = int(input())
for _ in range(n):
    s = input().strip()
    result = ''.join(mapping.get(ch, ch) for ch in s)
    print(result)