import math
n = int(input())
lcm = 2
for i in range(2, n+1):
#  print("i",i)
  lcm = i * (lcm)//math.gcd(i,lcm)
#  print("lcm",lcm)
print(lcm+1)
