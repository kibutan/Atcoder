n,k = list(map(int,input().split()))
h = list(map(int,input().split()))
dp = [float("inf")] * (n+1) #念の為多めに
dp[0] = 0
dp[1] = abs(h[1]-h[0])
for i in range(2,n):
    for j in range(1,min(k,i)+1):
        dp[i]  = min(dp[i], dp[i-j]+abs(h[(i-j)] -h[i]))

print(dp[n-1])
