# https://qiita.com/toast-uz/items/0d48813591193f331258
# ゼータ変換（累積和）、インライン、1〜2次元両用
def np_x_zeta(x, initial=None):
    if isinstance(x[0], list):
        for i in range(len(x)):
            np_x_zeta(x[i], initial=initial)
        if initial is not None:
            x.insert(0, [initial] * len(x[0]))
        for j in range(len(x[0])):
            for i in range(1, len(x)):
                x[i][j] += x[i - 1][j]
    else:
        if initial is not None:
            x.insert(0, initial)
        for i in range(1, len(x)):
            x[i] += x[i - 1]
 
# import numpy as np
n = int(input())
lr = [list(map(int,input().split())) for _ in range(n)]
lx,ly,rx,ry = [list(i) for i in zip(*lr)]
# print(rx)
cnt = [0]*(n+1)
# print(cnt)
desk = [[0 for _ in range(max(rx)+1)]for i in range(max(ry)+1)]
# desk_accx = [[0 for _ in range(max(rx)+1)]for j in range(max(ry)+1)]
# desk_accy = [[0 for _ in range(max(ry)+1)]for k in range(max(rx)+1)]
 
for i in range(n):
    desk[ly[i]][lx[i]] += 1
    desk[ry[i]][rx[i]] += 1
    desk[ly[i]][rx[i]] -= 1
    desk[ry[i]][lx[i]] -= 1
# for i in range(len(desk)):
    # print("Desk",desk[i])
np_x_zeta(desk)
 
# # print(min(ly),max(ry))
# for i in range(min(ly),max(ry)+1):
#     desk_accx[i] = list(accumulate(desk[i]))
 
 
# # print(np.array(desk_accx).T)
# for j in range(len(np.array(desk_accx).T)):
#     # print("accy[j]",np.array(desk_accx).T[j])
#     desk_accy[j] = list(accumulate((np.array(desk_accx).T)[j]))
#     # print(Counter(desk_accy[j]))
 
for i in range(max(ry)+1):
    for j in range(max(rx)+1):
        cnt[desk[i][j]] += 1
 
for i in range(1,n+1):
    print(cnt[i])
