n,x = list(map(int,input().split()))
a = list(map(int,input().split()))
ans= [i for i in a if not i == x]
 
print(*ans)
