dp = [float("inf")]*(100001)
n = int(input())
h = list(map(int,input().split()))

def jump(n):
  if n == 0:
    dp[n] = 0
  elif n == 1:
    dp[n] = min(dp[n],dp[n-1]+abs(h[n-1] - h[n]))
  else:
#    print("dp[n-1]",dp[n-1],"h[n-1]",h[n-1],"dp[n-2]",dp[n-2],"h[n-2]",h[n-2],)
    dp[n] = min(dp[n], int(dp[n-1]+abs(h[n-1] - h[n])), int(dp[n-2]+abs(h[n-2] - h[n])))
  return int(dp[n])

for i in range(n):
  jump(i)
#  if(i > 750):
#    print(i,dp[i])
print(dp[n-1])
