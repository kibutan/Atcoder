from itertools import product
import sys
input = sys.stdin.readline
r,c = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(r)]
a = list(zip(*a))
ans = 0
for i in product((0,1),repeat= r):
    sum = 0
#    print(i)
    for j in a:
        cnt = 0
#        print("j",j)
        for k in range(r):
#            print("a[k]",j[k],"i[k]",i[k])
            if(i[k] == j[k]):
                cnt += 1
#        print("sum",sum)
        sum += max(cnt,r-cnt)
    ans = max(ans,sum)
print(ans)




# for j in arr:
#     for i in range(r):
#         if(j[i]):first[i] = np.logical_xor(a[i],1).astype(np.int)
#         else:first[i] = a[i]
#         print(first[i])
#     print()
#     #縦方向でひっくり返すAwesome Code
#     # for col in range(c):
#     #     for row in range(r):
#     #         print("xor?",np.logical_xor(a,arr[0]).astype(np.int))
#     #         print("sum",sum(np.logical_xor(a,arr).astype(np.int)))
#     #         ans = max(ans, sum(np.logical_xor(a,arr).astype(np.int)))


# print("Test",ans)
