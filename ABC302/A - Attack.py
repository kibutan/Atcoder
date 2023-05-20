from math import ceil
a,h = list(map(int,input().split()))
[print(a//h) if a%h == 0 else print(a//h + 1)]
