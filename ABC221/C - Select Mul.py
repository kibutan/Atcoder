from itertools import product, repeat
n = input()
# a,b = list(map(int,input().split()))
# m = [list(map(int,input().split())) for i in range(n)]
ans = 0

for i in range(2**len(n)):
    bit = []
    for j in range(len(n)):
        left = []
        right = []
        rng = list(range(1,len(n)+1))
        if((i >> j)&1):
            bit.append(j+1)
            for k in bit:
                rng.remove(k)
            # print("rng",rng)
            # print("bit",bit)
            for k in bit:
                right.append(n[k-1])
            for k in rng:
                left.append(n[k-1])
            if(left == [] or right == []):break
            else:ans = max(ans,int("".join(sorted(right,reverse= True)))*int("".join(sorted(left,reverse= True))) )
# print(sorted(right,reverse= True),sorted(left,reverse= True))

            #     left = n[]
            #     print(n[k-1],end="")
            # print()
print(ans)
        # for k in bit:
        #     n_removed = n.replace(str(k),"")
        #     print("n_rep",n_removed)

