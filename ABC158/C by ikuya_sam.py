#なるほどと思った答え
#https://atcoder.jp/contests/abc158/submissions/21174959

import math 
a, b = map(int, input().split())
 
x = set(range(math.ceil(100/8*a),  math.floor(100/8*(a+1))))
y = set(range(math.ceil(100/10*b), math.floor(100/10*(b+1))))
cand = x&y
if cand:
    print(min(cand))
else:
    print(-1)
