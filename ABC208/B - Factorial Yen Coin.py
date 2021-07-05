from math import factorial
p = int(input())
# 10**7はせいぜい11!以下
cnt = 0 
ans = 0
for i in range(11,0,-1):
    if(factorial(i) == 1):
        ans += p
        break
    if(factorial(i) <= p):
        cnt = p//factorial(i)
        p -= cnt * factorial(i)
        ans += cnt
print(ans) 
