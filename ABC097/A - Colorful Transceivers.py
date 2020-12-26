a,b,c,d = list(map(int,input().split()))
if((abs(b-a) <= d and abs(b-c)<=d) or (abs(c-a) <= d)):print("Yes")
else:print("No")
