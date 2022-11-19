from collections import deque

n,k = map(int,input().split())
a = list(map(int,input().split()))

a_deque = deque(a)

for i in range(k):
    a_deque.popleft()
    a_deque.append(0)
print(*list(a_deque))
