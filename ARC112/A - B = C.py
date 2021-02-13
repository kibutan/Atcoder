t= int(input())
lr = [map(int, input().split()) for _ in range(t)]
l, r = [list(i) for i in zip(*lr)]
ans = 0

#for i in range(t):
#  for j in range(1, (r[i]-(2*l[i]))+2 ):
#    ans += j
#  print(ans)
#  ans = 0
for i in range(t):
  if(l[i] == r[i] and l[i] != 0): print(0)
  else:print(((1+(r[i]-2*l[i]))*(r[i]-2*l[i])//2 ) + (1+(r[i]-2*l[i])) )
