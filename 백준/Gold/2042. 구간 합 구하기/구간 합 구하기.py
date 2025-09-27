# goldI_2042
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split()) # 수 개수, 변경 횟수, 구간 합 횟수
treeHeight = 0
length = n

while length != 0:
    length //= 2
    treeHeight += 1
treeSize = pow(2, treeHeight + 1)
leftNodeStartIndex = treeSize // 2 - 1
tree = [0] * treeSize

for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + n + 1):
    tree[i] = int(input())

def setTree(i):
    while i != 1:
        tree[i // 2] += tree[i]
        i -= 1
setTree(treeSize - 1)

def changeVal(index,value):
    diff = value - tree[index]
    while index > 0:
        tree[index] += diff
        index //= 2

def getSum(s, e):
    partSum = 0
    while s <= e:
        if s % 2 == 1:
            partSum += tree[s]
            s += 1
        if e % 2 == 0:
            partSum += tree[e]
            e -= 1
        s //= 2
        e //= 2
    return partSum

for _ in range(m+k):
    q, s, e = map(int, input().split())
    if q == 1:
        changeVal(leftNodeStartIndex + s, e)
    elif q == 2:
        s += leftNodeStartIndex
        e += leftNodeStartIndex
        print(getSum(s, e))