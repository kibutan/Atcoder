n=int(input())
s = input()
MOD = 10**9 + 7
dp=[[0 for i in range(len(s)+1)] for _ in range(8)]
string = "atcoder"
for i in range(len(s)+1):
    dp[0][i] = 1

for i in range(7):
    for j in range(len(s)):
        if(string[i] == s[j]):dp[i+1][j+1] = (dp[i+1][j] + dp[i][j] )% MOD
        else:dp[i+1][j+1] = dp[i+1][j]
    # print(string[i],":",dp[i])
# print(string[-1],":",dp[-1])
print(dp[-1][-1])
