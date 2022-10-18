n,x = map(int,input().split())
a_list = list(map(int,input().split()))
a = [i for i in range(n) if i%2 == 0]
b = [i for i in range(n) if i%2 == 1]

ans = sum(a) + sum(b) - len(b)
if(ans <= x):
  print("Yes")
  exit()
print("No")
