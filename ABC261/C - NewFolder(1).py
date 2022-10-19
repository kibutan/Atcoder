from collections import deque

n = int(input())
s = deque([input() for _ in range(n)])
history = {}

for i in range(n):
    query = s.popleft()
    if(query in history):
        print(query + "(" + str(history[query] + 1) +")"  )
        history[query]+=1
    else:
        print(query)
        history[query]=0
    # print(history)
