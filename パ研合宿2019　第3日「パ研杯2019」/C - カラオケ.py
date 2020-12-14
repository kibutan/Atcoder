N,M = list(map(int,input().split()))
A = [list(map(int,input().split())) for _ in range(N)]
#print(N)
#print(M)
#print(A)
score1 = [0]*M

for i in range(M):
  score1[i] = [r[i] for r in A]
score2 = 0
ans = 0
i = 0
#print(score1)


#for i in range():
for i in range(0,M-1):
  for j in range(1, M):
    for k in range(N):
#        ans = max(ans, max(score[])+max()+max())
#      print("[k][i], k: "+str(k)+" i: "+str(i)+" score: "+str(score1[i][k]))
#      print("[k][j], k: "+str(k)+" j: "+str(j)+" score: "+str(score1[j][k]))
      ans += max(score1[i][k],score1[j][k])
    score2 = max(score2,ans)
    ans = 0
print(score2)
    









#for k in range(N):
#  score1.append(A[k][0])

#for i in range(M): #→
#  score1[i] = A[j][i]
#  print(score1)
#  for j in range(N): #↓
#    score2.append(A[j][i])
#    ans = max(ans,sum(max(score1[0], score2[0]),max(score1[1], score2[1]),max(score1[2], score2[2])))
#  score2 = score1
#print(score2)
