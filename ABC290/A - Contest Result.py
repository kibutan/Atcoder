n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
sum = 0
for i in b:
  sum += a[i-1]
print(sum)
