n = int(input())
a = list(input().split())
b = list(input().split())
ans = 0
ans2 = 0


for i in range(n):
    if(a[i] == b[i]):ans += 1
    elif(a[i] in set(b)):ans2+=1
print(ans)
print(ans2)
