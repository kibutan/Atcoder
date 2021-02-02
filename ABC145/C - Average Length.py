import math
from decimal import Decimal
import itertools
n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]
distance = 0
ans = 0
number = 0 
cnt = 0

##################################permutations
#permutations_lis = itertools.permutations(xy)
#for one_case in permutations_lis: 
#  for num in one_case:
#    print(num, end=" ")
#  print("")
###############################################

perlis=[]
permutations_lis = itertools.permutations(xy)
for one_case in permutations_lis: 
  for num in one_case:
    perlis.append(num)
  cnt += 1
#  print(cnt)
#  print(perlis)
  #都市間の距離をだしたい。距離は都市-1 ; 最後の都市-最初の都市 となる
  #My Awesome Code 
  for i in range(0,len(perlis)-1):
#    print("now",perlis[i],"next",perlis[i+1])
#    print("dis",math.sqrt(  (perlis[i+1][0] - perlis[i][0])**2 + (perlis[i+1][1] - perlis[i][1])**2  )) 
    distance += Decimal(math.sqrt(  (perlis[i+1][0] - perlis[i][0])**2 + (perlis[i+1][1] - perlis[i][1])**2  ))
#  print("now",perlis[-1],"next",perlis[0])
#  print("dis",math.sqrt(  (perlis[0][0] - perlis[-1][0])**2 + (perlis[0][1] - perlis[-1][1])**2  )) 
#  print("distance",distance)
#  distance += Decimal(math.sqrt(  (perlis[0][0] - perlis[-1][0])**2 + (perlis[0][1] - perlis[-1][1])**2  ))
#  print("distance",distance)
#  print()
  perlis = []
#print("ans",Decimal(distance/cnt))
print(Decimal(distance/cnt))

