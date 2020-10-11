N = list(map(int,input().split()))
sort = sorted(N)
tasty_big = sum(N)
tasty_low = 0
if(sort[3] == sort[2]+sort[1]+sort[0]):print("Yes")
elif(sort[3] + sort[2] == sort[1] + sort[0]):print("Yes")
elif(sort[3] + sort[1] == sort[2] + sort[0]):print("Yes")
elif(sort[3] + sort[0] == sort[2] + sort[1]):print("Yes")
else:print("No")
