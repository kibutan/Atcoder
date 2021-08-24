n = int(input())
s = [input() for _ in range(n)]
check = set()
# set_s = sorted(set(s), key = s.index)
ans = 1
for i in s:
    if(i in check):
        ans+=1
        continue
    else:
        print(ans)
        check.add(i)
        ans+=1
