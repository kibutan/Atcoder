from collections import deque
import sys
input = sys.stdin.readline

n,k = list(map(int,input().split()))
c= list(map(int,input().split()))
queue = deque([])

for i in range(k):
    queue.append(c[i])
# print(queue)
cnt = len(set(queue))

for i in range(k,n):
    # print(queue.popleft())
    queue.popleft()
    queue.append(c[i])
    cnt = max(cnt,len(set(queue)))
# print(queue)
print(cnt)
