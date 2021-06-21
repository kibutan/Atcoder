n = int(input())
# a,b = list(map(int,input().split()))
# m = [list(map(int,input().split())) for i in range(n)]

ok = 10**9+1
ng = 0

def is_ok(middle):
    if(1 + middle)*middle//2 >= n:
        return True
    else:return False

while ok - ng >1:
    middle = (ok + ng)//2
    # print((1 + middle)*middle//2 , n)
    # print(ok,ng)
    if is_ok(middle):ok=middle
    else:ng = middle
print(ok)
