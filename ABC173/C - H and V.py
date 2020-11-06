import sys
H,W,K = list(map(int,input().split()))
c = [[str(c) for c in H.strip()]for H in sys.stdin]
print(c)
