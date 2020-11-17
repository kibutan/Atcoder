import collections
ans = 0
count = 0
N = int(input())
S_n = [input() for _ in range(N)]
C_n = collections.Counter(S_n)
#print(C_n)

M = int(input())
S_m = [input() for _ in range(M)]
C_m = collections.Counter(S_m)
#print(list(C_m.values()))
#print(C_m.get("apple"))

for i in C_n:
  count = C_n.get(i)-C_m.get(i,0)
  ans = max(ans,count)
print(ans)

#  print(i+"="+str(()))
  
