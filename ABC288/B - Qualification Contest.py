n,k = map(int,input().split())
s = [input() for _ in range(n)]
for name in sorted(s[:k]):
  print(name)
