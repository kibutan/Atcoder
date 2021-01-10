n = int(input())
a = list(map(int,input().split()))
ans = a
temp = []
while len(a) > 2:
  for i in range(0,2**n,2):
#    print("i",i)
    temp.append(max(a[i],a[i+1]))
  a = temp
#  print(temp)
  temp=[]
  n -= 1
#  print("len",len(a))
#print(temp)
print(ans.index(min(a))+1)
