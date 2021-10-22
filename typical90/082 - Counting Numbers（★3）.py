l,r = list(map(str,input().split()))
div = 10**9+7
ans = 0
# print(len(l),len(r),int(r)-int(l))
left = 0
right = 0
# print(type(int(l)),type(l),int(l)+int(r))
 
for i in range(len(l),len(r)+1):
    if i == len(l):left = int(l)
    else:left = 10**(i-1)
    if i == len(r):right = int(r)
    else:right = (10 ** (i))-1
 
    ans += (i * ((right - (left-1))%div)*((right + left)%div)//2)%div
print(ans%div)
