from itertools import combinations
n = int(input())
abcde = [list(map(int,input().split())) for _ in range(n)]
before = 0
for teams in combinations(abcde,3):
  pow = max(teams[0][0],teams[1][0],teams[2][0])
  spd = max(teams[0][1],teams[1][1],teams[2][1])
  tec = max(teams[0][2],teams[1][2],teams[2][2])
  int = max(teams[0][3],teams[1][3],teams[2][3])
  idea = max(teams[0][4],teams[1][4],teams[2][4])
  total = min(pow,spd,tec,int,idea)
  if(before >= total):continue
  else:before = total
print(before)
