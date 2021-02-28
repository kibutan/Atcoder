n = int(input())
sq = int(n**0.5)
s =set()
for i in range(2,sq+1):
  x = i*i
  while x <= n:
#    print(x)
    s.add(x)
    x = x*i
print(n - len(s))
