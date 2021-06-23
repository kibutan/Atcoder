import sys
input = sys.stdin.readline

h,w = list(map(int,input().split()))
a = [list(map(int,input().split()))for _ in range(h)]
ans = {}
w_sum = {}
h_sum = {}

for i in range(h):
    w_sum[i] = sum(a[i])
b = list(zip(*a))

for j in range(w):
    h_sum[j] = sum(b[j])

def solve(i,j):
    return w_sum[i]+h_sum[j] - a[i][j]

for i in range(h):
    for j in range(w):
        # print("→",w_sum[i],"↓",h_sum[j],".",a[i][j],end = "      ")
        print(solve(i,j),end = " ")
    print()
