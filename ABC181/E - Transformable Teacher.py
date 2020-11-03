import math
N = list(map(int,input().split()))
H = list(map(int,input().split()))
W = list(map(int,input().split()))
ans = 100000001
#pair_list = []
#print(H)
for i in W:
  Pair_list = [i]
  Pair_list = sorted(Pair_list + H)
#  print(Pair_list)
  ans = min(ans, int(math.fabs(sum(Pair_list[0::2])-sum(Pair_list[1::2]))))
print(ans)
  
