N = int(input())
A = list(map(int,input().split()))
Ruisekiwa = [0]*(len(A)+1)
for k in range(len(A)):
  Ruisekiwa[k+1] = Ruisekiwa[k]+A[k]
ans = 0
for i in range(N-1):
  ans += A[i]*(Ruisekiwa[len(Ruisekiwa)-1]-Ruisekiwa[i+1])
print(ans%(1000000007))
  
