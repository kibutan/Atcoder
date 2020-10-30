N = list(map(int,input().split()))
forbidden_list = []
ans = 101
if N[1] == 0:print(N[0])
else:
  p = list(map(int,input().split()))
  forbidden_list = list(range(0 ,102))
#  print(forbidden_list)
  forbidden_list = sorted(set(forbidden_list)^set(p),reverse=True)
#  print(forbidden_list)
  for i in range(len(forbidden_list)):
    ans = min(ans,abs(N[0]-forbidden_list[i]))
  if((N[0]-ans) in forbidden_list):print(N[0]-ans)
  else:print(N[0]+ans)
