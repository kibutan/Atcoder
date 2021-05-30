import numpy as np
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
a = np.array([list(map(int,input().split())) for _ in range(n)])
ans = float("inf")
index = (k**2//2)+1

def mid(grid):
    array = sorted(grid.flatten())
    return array[-index] 

for i in range(0,n-(k-1)):
    for j in range(0, n-(k-1)):
        if(np.min(a[i:i+k,j:j+k]) >= ans):continue
        else:ans = min(ans,mid(a[i:i+k,j:j+k]))
print(ans)
