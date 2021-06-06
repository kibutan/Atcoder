from itertools import product
n,m = map(int,input().split())
if m  == 0 : 
    print(n)
    exit()
# print(m)
ab = [map(int,input().split()) for _ in range(m)]
a,b = [set(i) for i in zip(*ab)]
print(type(a))
print(a)
print(b)
ans = 0
route = list(product(a,b))
cnt = len(route)
print(route)
print("ab",a^b)

# cnt += a^b
print(cnt)
