a,b,c = list(map(int,input().split()))
div = 998244353
print(((a*(1+a)//2) *(b*(1+b)//2) *(c*(1+c)//2)) % div  )
