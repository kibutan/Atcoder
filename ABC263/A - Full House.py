a,b,c,d,e =  sorted(map(int,input().split()))
if(len(set([a,b,c,d,e])) == 2 and a==b and d==e):
  print("Yes")
else:
  print("No")
