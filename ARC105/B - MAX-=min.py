N = int(input())
A = list(map(int,input().split()))
while(min(A) != max(A)):
  maxIndex = [i for i, x in enumerate(A) if x == max(A)]
  for i in range(len(maxIndex)):
    A[maxIndex[i]] = A[maxIndex[i]] - min(A)
  if(min(A) == max(A)):break
print(A[0])
#最大値のIndexを返す関数MaxIndex
