a,b,c = sorted(list(map(int,input().split())))
odd = 0
even = 0
ans = 0
if(a%2 == b%2 == c%2):print(int(((c-b)+(c-a))/2))
else:
  if(a%2 == b%2):
    a += 1
    b += 1
  elif(a%2 == c%2):
    a += 1
    c += 1
  elif(b%2 == c%2):
    b += 1
    c += 1
  print(int(((c-b)+(c-a))/2)+1)  
