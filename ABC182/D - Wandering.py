N = int(input())
A = list(map(int,input().split()))
ans = 0
x = 0

Ruisekiwa = [0]*(len(A)+1)
for k in range(len(A)):
  Ruisekiwa[k+1] = Ruisekiwa[k]+A[k]
#print(Ruisekiwa)

q = [0]*(len(A)+1)


for i in range(0,N+1):
  p = sum(A[0:i])
#  print("p:"+str(p))
  q[i] = max(Ruisekiwa[0:i+1])
#  print("q:"+str(q))
  ans = max(ans, x+q[i])
  x += p
print(ans)
#  q = 
