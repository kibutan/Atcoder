import bisect
n,l = list(map(int, input().split()))
k = int(input())
a = list(map(int, input().split()))+[l]
ok = 0
ng = l+1

def is_ok(middle):
    global ok,ng
    if(step2(middle)):ok = middle
    else : ng = middle
#Answer = m
#step2
def step2(middle):
    cnt = 0
    prev = 0
    for i in a:
        if( (i - prev) >= middle ): 
            cnt += 1
            prev = i
    if(cnt >= k+1):return True
    else:return False

while ng - ok > 1:
    middle = (ng + ok)//2
    is_ok(middle)

print(ok)
