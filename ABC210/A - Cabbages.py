n,a,x,y = list(map(int,input().split()))
if n <= a: print(n*x)
else: print(a*x+y*(n-a))
