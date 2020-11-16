import collections
import itertools
N,M = list(map(int, input().split()))
a = [list(map(int,input().split())) for _ in range(M)]
road_list = list(itertools.chain.from_iterable(a))
count = collections.Counter(road_list)
for i in range(1,N+1):print("" + str(road_list.count(i)))
