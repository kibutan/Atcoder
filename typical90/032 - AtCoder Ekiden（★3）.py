from itertools import permutations
n = int(input())
# hate = [[False for _ in range(n)]for _ in range(n+1)]
hate = [[False for _ in range(n)]for _ in range(n)]
a = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
xy = [list(map(int,input().split())) for _ in range(m)]
if m != 0:x, y = [list(i) for i in zip(*xy)]
 
for i in xy:
    hate[i[0]-1][i[1]-1] = True
    hate[i[1]-1][i[0]-1] = True
 
# print(hate)
 
# ans = float("inf")
# for i in permutations(a):
#     cnt = 0
#     sum = 0
#     print(i)
#     for j in i:
#         print(j[cnt])
#         sum += j[cnt]
#         cnt += 1
#     ans = min(ans,sum)
# print(ans)
ans = float("inf")
for i in permutations(range(n)):
    # cnt = 0
    sum = 0
    # print(i)
    for j in range(len(i)-1):
        if(hate[i[j]][i[j+1]]):
            # print("hate",hate[i[j]])
            break
    else:
        for k in range(len(i)):
            # print("time",a[i[k]][k])
            sum += a[i[k]][k]
        ans = min(ans,sum)
if ans == float("inf"):ans = -1
 
print(ans)
 
 
    
