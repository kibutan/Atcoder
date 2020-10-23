A = list(map(int,input().split()))
sum = 0 
for i in range(A[0], A[1]+1,1):
  if(str(i)[::-1] == str(i)):sum += 1
print(sum)
