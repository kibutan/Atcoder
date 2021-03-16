a,b = list(map(int,input().split()))
hight = 0
for i in range(1,(b-a)):
  hight += i
print(hight-a)
