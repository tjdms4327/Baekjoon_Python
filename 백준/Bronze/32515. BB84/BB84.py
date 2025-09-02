import sys
input = sys.stdin.readline

n = int(input())
j_vh = input().strip()
j_01 = input().strip()
i_vh = input().strip()
i_01 = input().strip()

j_s = ''.join(j_01[i] for i in range(n) if j_vh[i] == i_vh[i])
i_s = ''.join(i_01[i] for i in range(n) if j_vh[i] == i_vh[i])
print(i_s if j_s == i_s else 'htg!')