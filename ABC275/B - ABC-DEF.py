a,b,c,d,e,f = map(int,input().split())
# print(a)
div = 998244353

print(( ((a%div) * (b%div) * (c%div) % div) - ((d%div) * (e%div) * (f%div) % div)  ) %div)
