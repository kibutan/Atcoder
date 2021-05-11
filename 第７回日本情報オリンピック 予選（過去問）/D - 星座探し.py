## LISTを使っているので遅い。https://atcoder.jp/contests/joi2008yo/submissions/22510706
## Testcase通過823 ms。

m = int(input())
aim =[list(map(int,input().split())) for _ in range(m)]
# aim =[tuple(map(int,input().split())) for _ in range(m)] 
# aim_set = set(aim)
 
n=int(input())
pic = [list(map(int,input().split())) for _ in range(n)]
# pic = [tuple(map(int,input().split())) for _ in range(n)] 
# pic_set=set(aim)
 
delta = []
for i in pic:
    delta.append([i[0]-aim[0][0],i[1]-aim[0][1]])
#print(delta)
 
for i in delta:
    cnt = 0
    for j in aim:
        pan = [j[0]+i[0],j[1]+i[1]]
        if not(pan in pic):break
        else: cnt += 1
    if(cnt == m):
        print(i[0],i[1])
        exit()
    else:continue
 
