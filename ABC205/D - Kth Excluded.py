import bisect
 
# n = int(input())
n,q = list(map(int,input().split()))
a = list(map(int,input().split()))
k = [int(input()) for i in range(q)]
# k_inv = [i for i in range(1,10**18+1)]^[k]
a_set = set(a)
# print(k_inv[1:10])
bias = 0
def query(n):
    global a_set,a,bias
    index = bisect.bisect_right(a,n)
    index_2 = bisect.bisect_right(a,n+index)
    ans = 0
    if(index == index_2):
        if(bias != 0):
            ans = n + bias
            bias = 0
            return ans
        else:return n+index
    else:
        if(bias == 0):
            bias = index
        return query(n+1)
 
for i in k:
    print(query(i))
