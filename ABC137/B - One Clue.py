K,X = list(map(int,input().split()))
list = []
if(K == 1):print(X)
else:
  for i in range(2*K-1):
    print(X-(K-1) + i,end =" ")
