# bronzeI_15819
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
words = [input().strip() for _ in range(n)]
words.sort()

print(words[l-1])