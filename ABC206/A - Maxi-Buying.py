n = int(input())
# a,b = list(map(int,input().split()))
# m = [list(map(int,input().split())) for i in range(n)]

ans = int(n * 1.08)
# print(ans)
if(ans > 206):print(":(")
elif(ans == 206):print("so-so")
else:print("Yay!")
