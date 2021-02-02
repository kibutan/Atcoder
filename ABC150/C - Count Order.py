import itertools
n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
origin_list = []
compare_list =[]
cnt = 0 

p_order,q_order = 0,0
if(p == q):
  print(0)
  exit()

for i in range(n):
  origin_list.append(i+1)
permutation_lis = itertools.permutations(origin_list)
for one_case in permutation_lis:
  for num in one_case:
    compare_list.append(num)
  #Great Code HERE
#  print(compare_list)
#  print(compare_list == p)
  cnt+=1
#  print(cnt)  
  if(compare_list == p):p_order = cnt
  elif(compare_list == q):q_order = cnt
  compare_list = []
#print("p",p)
#print("q",q)  
print(abs(p_order - q_order))
