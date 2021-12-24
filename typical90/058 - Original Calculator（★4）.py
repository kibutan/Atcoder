from collections import defaultdict
n,k = map(int,input().split())
mod = 10**5
visit_hist = defaultdict(lambda:False)
cycle = 0

def push_a(x):
    global k
    # print("x first",x)
    y = sum(list(map(int,str(x))))
    x = (x+y)%mod
    return x

for i in range(1,k+1):
    n = push_a(n)
    if not visit_hist[n]:
        visit_hist[n] = i
    else:
        term = (i - visit_hist[n])
        div = (k - visit_hist[n]) % term + visit_hist[n]
        if term == 1:
            print(n)
            exit()
        ans = [k for k , v in visit_hist.items() if v ==  div][0]
        print(ans)
        exit()
    # print(n,visit)
print(n)
