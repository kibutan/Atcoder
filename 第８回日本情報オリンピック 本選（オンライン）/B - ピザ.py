d = int(input())
n = int(input())
m = int(input())
stores = [0,d]
delivery = []
ans = 0

def calc_dist(st,deli,num):
  print("st",st,deli,num)
  left = 0  # index of left
  right = num # index of right
  before_l = 0
  before_r = 0
  dist = float("inf")
  while left < right:
    print("Before l and R",before_l,left , before_r,right)
    if(before_l == left and before_r == right):break
    mid = int((left+right)/2) #index of s[mid]
    print("left:",st[left]," right:",st[right],"mid",st[mid])
    if(st[mid] == deli):
      print("return",0)
      return 0
    elif(deli > st[mid]):
      print("deli > st[mid]",deli,st[mid])
      before_l = left
      before_r = right
      left = int((left+right)/2) + 1
      print("left:",st[left]," right:",st[right],"mid",st[mid])
    else: 
      print("deli < st[mid]",deli,st[mid])
      before_r = right
      before_l = left
      right = int((left+right)/2)
      print("left:",st[left]," right:",st[right],"mid",st[mid])
  print("left-deli",abs(st[left] - deli),"right-deli",abs(st[before_l] - deli))
  print("return",min(abs(st[left] - deli),abs(st[before_l] - deli)))
  return min(abs(st[left] - deli),abs(st[before_l] - deli))

for i in range(n-1):
  stores.append(int(input()))
stores.sort()
for i in range(0,m):
  delivery.append(int(input()))
#delivery.sort():
for i in range(0,m):
  print("i",i,delivery[i])
  ans += calc_dist(stores,delivery[i],n)
  
print(ans,end="")
print(d,n,m,stores,delivery)
