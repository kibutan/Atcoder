from decimal import Decimal
n = int(input())
length = len(str(n))
ans = 0
for i in range(1,10**(length//2)):
#  print(int(str(i)+str(i)))
  if n >= int(str(i)+str(i)):ans+=1
#print(int(str(i)+str(i)))
print(ans)
