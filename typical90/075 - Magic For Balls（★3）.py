N = int(input())
prime_list = []
def prime(n):
    i = 2
    ans=dict()
    n=N
    while i*i <=N:
        while n%i==0:
            n=n//i
            if i in ans:
                ans[i]+=1
            else:
                ans[i]=1
        i+=1
    if n!=1:
        ans[n]=1
    if((len(list(ans.items()))) == 1 and N in ans):return [0]
    # print(len(list(ans.items())))
    # print(ans.values())
    return (list(ans.values()))

prime_sum = sum(prime(N))
# print(prime_sum)
for i in range(37):
    if(2**i >= prime_sum):
        print(i)
        exit()
    
# for i in prime_list:
