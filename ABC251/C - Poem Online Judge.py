n = int(input())
st = list(map(str, input().split()) for _ in range(n))
s,t =list(zip(*st))
# print(t)
score_MAX = 0
index_MAX = 0
original = set()

for i in range(n):
    if s[i] in original:continue
    else:
        original.add(s[i])
        if score_MAX < int(t[i]):
            score_MAX = int(t[i])
            index_MAX = i
print(index_MAX+1)
