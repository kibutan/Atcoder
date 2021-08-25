from collections import deque
q = int(input())
tx = [list(map(int,input().split())) for _ in range(q)]
t,x = [list(i) for i in zip(*tx)]
# print(t,x)
que = deque()
# Upper <--> Lower

for i in range(q):
    if(t[i] == 1):que.appendleft(x[i])
    elif(t[i] == 2):que.append(x[i])
    elif(t[i] == 3):print(que[x[i] - 1])
