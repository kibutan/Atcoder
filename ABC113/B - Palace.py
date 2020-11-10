N = int(input())
T, A = list(map(int,input().split()))
H = list(map(int,input().split()))
ans = [0] * len(H)
for i in range(N):
#  print(A - H[i]*0.006)
  ans[i] =(A*1000) - (T*1000-(H[i]*6))
  if(ans[i]<0):ans[i] *= -1  
print(ans.index(min(ans))+1)
