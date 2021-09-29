def cmb(n,r, mod):
    if(r < 0 or r > n):
        return 0
    r = min(r,n-r)
    return g1[n] * g2[r] *g2[n-r] %mod
mod  = 10**9+7
N = 10**6
g1 = [1,1]
g2 = [1,1]
inv = [0,1]

for i in range(2, N +1):
    g1.append((g1[-1] * i) % mod)
    inv.append( ( -inv[mod%i] *  (mod //i) )% mod)
    g2.append( (g2[-1] * inv[-1] % mod) )

n,l = map(int,input().split())
ans = 1 #すべて1段づつ登る場合を既に入れておく
for i in range(1,(n//l)+1): # i をnCiとして利用
    if(n-l < 0):break
    elif(n-l == 0):
        ans += 1
        break
    else:
        n = n-l+1
        ans += cmb(n,i,mod)
print(ans%mod)
