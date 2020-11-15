from decimal import Decimal
S_x,S_y,G_x,G_y =list(map(int, input().split()))
delta_x = G_x-S_x
delta_y = G_y+S_y
#print(str(delta_x)+","+str(delta_y))
alpha = Decimal(delta_y/delta_x) #傾き
#print(alpha)
ans = Decimal(S_y / alpha)
print(ans+S_x)
