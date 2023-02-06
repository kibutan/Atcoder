n = int(input())
ab = [map(int,input().split()) for _ in range(n)]
for a,b  in ab:
  print(a+b)
