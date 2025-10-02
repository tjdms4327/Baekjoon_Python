# goldI_11505
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
treeHeight = 0
length = n
MOD = 1000000007

while length != 0:
    length //= 2
    treeHeight += 1

treeSize = pow(2, treeHeight+1)
leftNodeStartIndex = treeSize // 2 - 1
tree = [1] * treeSize

for i in range(leftNodeStartIndex+1, leftNodeStartIndex+n+1):
    tree[i] = int(input())

def setTree(i):
    while i != 1:
        tree[i//2] = tree[i//2] * tree[i] % MOD
        i -= 1
setTree(treeSize - 1)

def changeVal(index, value): # 값 변경
    tree[index] = value
    while index > 1:
        index //= 2
        tree[index] = tree[index*2] % MOD * tree[index*2+1] % MOD

def getMul(s, e): # 구간 곱 계산
    partMul = 1
    while s <= e:
        if s % 2 == 1:
            partMul = partMul * tree[s] % MOD
            s += 1
        if e % 2 == 0:
            partMul = partMul * tree[e] % MOD
            e -= 1
        s //= 2
        e //= 2
    return partMul 

for _ in range(m+k):
    q, s, e = map(int, input().split())
    if q == 1:
        changeVal(leftNodeStartIndex+s, e)
    elif q == 2:
        s += leftNodeStartIndex
        e += leftNodeStartIndex
        print(getMul(s, e))