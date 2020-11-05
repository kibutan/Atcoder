N = int(input())
A = list(map(int,input().split()))
ans = 0
for i in range(N-1):
#  print("i:"+str(i))
  for j in range(i+1,N):
#    print("j:"+str(j))
#    print(str(A[i]*A[j]))
    ans += (A[i]*A[j])
print(ans%(1000000007))
  
