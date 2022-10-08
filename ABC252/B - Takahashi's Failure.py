n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a_max = [i for i , v in enumerate(a) if v == max(a)]

for i in a_max:
  if(i+1 in b):
    print("Yes")
    exit()
print("No")
