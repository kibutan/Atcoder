N,M,K = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A_cnt = 0
B_cnt = 0
ans = 0
time = 0
if(time < K )
for i in range(N+M):
  if(A[A_cnt] < B[B_cnt]):
    ans += 1
    time = A[A_cnt]
    A_cnt += 1
  else:
    ans += 1
    time = B[B_cnt]
    B_cnt += 1
print(ans)
