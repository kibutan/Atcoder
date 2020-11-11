N,K = list(map(int,input().split()))
ans = 0
while(K**ans <= N):ans += 1
#if(N == (N//K) N%K == 0):ans +=1
print(ans)
