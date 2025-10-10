# bronzeIII_13627
import sys
input = sys.stdin.readline

n, r = map(int, input().split())
comeBack = set(map(int, input().split()))

volunteer = set(range(1, n+1))
diff = sorted(volunteer - comeBack)
print(*(diff or ['*']))