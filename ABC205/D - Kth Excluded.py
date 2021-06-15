import bisect
 
# n = int(input())
n,q = list(map(int,input().split()))
a = list(map(int,input().split()))
k = [int(input()) for i in range(q)]
# k_inv = [i for i in range(1,10**18+1)]^[k]
a_set = set(a)
# print(k_inv[1:10])
def query(n):
    global a_set
    index = bisect.bisect_right(a,n)
    if(n + index not in a_set):return n + index
    else:return query(n+1)
 
for i in k:
    print(query(i))
