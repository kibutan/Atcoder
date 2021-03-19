import bisect
import collections

N = int(input())
A = list(map(int,input().split()))
A.sort()
print(A)
B = list(map(int,input().split()))
B.sort()
print(B)
C = list(map(int,input().split()))
#C.sort()
#print(C)

ans = 0
ab = []
bc = []
for j in range(N):
  if(bisect.bisect_left(B,C[j])!=0):
    bc.append(bisect.bisect_left(B,C[j]))
  if(bisect.bisect_left(A,B[j])!=0):
    ab.append(bisect.bisect_left(A,B[j]))
print(bc)
print(ab)
# BとAの関係も辞書かしたほうが早いのでは？
cnt_bc = collections.Counter(bc)
cnt_ab = collections.Counter(ab)

print(cnt_bc)
print(cnt_ab)

#for i in bc:
#  ans += bisect.bisect_left(A,B[i-1])
#print(ans)
for j in cnt_bc:
#  print("j",j)
  for i in range(j):
#    print(j)
#    print("i:",i," bug:",(bisect.bisect_left(A,B[j-1]-1-i)))
#    print("B[",j-1-i,"](",B[j-1-i],")以下のAの数",bisect.bisect_left(A,B[j-1-i]))
    ans += (bisect.bisect_left(A,B[j-1-i]) * cnt_bc[j])

#for j in range(N):
#  print("C[j]",C[j])
#  print("C[j]以下のBの数",bisect.bisect_left(B,C[j]))
#  if(bisect.bisect_left(B,C[j])!=0):
#    for i in range(bisect.bisect_left(B,C[j])):
#    print("i:",i," bug:",(bisect.bisect_left(B,C[j]))-1-i)
#    print("C[J]以下のB[？]以下のAの数",bisect.bisect_left(A,B[bisect.bisect_left(B,C[j])-1-i]))
#      ans += (bisect.bisect_left(A,B[bisect.bisect_left(B,C[j])-1-i]))
print(ans)
