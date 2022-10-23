h,w = map(int,input().split())
c = [input() for _ in range(h)]
# print(c)

for i in range(w):
    ans = 0
    column = [r[i] for r in c]
    print(column.count("#"))
