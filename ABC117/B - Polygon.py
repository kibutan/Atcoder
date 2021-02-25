n = int(input())
l = list(map(int,input().split()))
if((sum(l)-max(l)) <= max(l)):print("No")
else:print("Yes")
