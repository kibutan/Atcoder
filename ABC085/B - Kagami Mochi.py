import collections
N = int(input())
d = [int(input()) for i in range(N)]
print(len(collections.Counter(d)))
