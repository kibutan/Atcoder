k = int(input())
div = 10**9+7
n = 0
ans = 0
dp = [0]*(k+1)
if(k%9 != 0):ans = 0
else:
    dp[0]=1
    dp[1]=1
    for i in range(2,k+1):
        for j in range(1,10):
            dp[i]+=dp[i-j]
        dp[i] %= div
    ans = dp[k]
print(ans)
