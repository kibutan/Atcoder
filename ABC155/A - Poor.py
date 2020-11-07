a,b,c = list(map(int, input().split()))
if(a == b and a == c):print("No")
elif(a != b and a != c and b!= c):print("No")
else:print("Yes")
