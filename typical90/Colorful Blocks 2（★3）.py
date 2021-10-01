n,k = list(map(int,input().split()))
div = 10**9+7
if(n == 1):print(k)
elif(n == 2):print(k*(k-1))
elif(k<3):print(0)
else:print(((k*(k-1)%div)*pow(k-2,n-2,div))%div)
