n,m,x,t,d = list(map(int,input().split()))
# b(cm) + D*X
if( x<=m ):print(t)
else:print( t-(x-m)*d )
