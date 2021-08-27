n= int(input())
a,b,c=sorted(map(int,input().split()))
ans = 10000
c_max_coins = n//c

for i in range(c_max_coins+1):
    b_max_coins = (n-(c*i))//b
    # if b_max_coins <0: break
    for j in range(b_max_coins+1):
        remain = n-((c*i)+(b*j))
        if remain < 0:continue
        # for k in range(n-(c*i)-(b*j)//a):
        #    if((i*a)+(j*b)+(c*k) == n and i+j+k < ans):ans = i+j+k
        if(remain % a == 0):ans = min(ans,i+j + remain/a)
print(int(ans))

