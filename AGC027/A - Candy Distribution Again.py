N,x = list(map(int,input().split()))
a = sorted(list(map(int,input().split())))
ans = -1
Ruisekiwa = [0]*(len(a)+1)
for i in range(len(a)):
  Ruisekiwa[i+1] = Ruisekiwa[i]+a[i]
for j in range(len(Ruisekiwa)):
  if(Ruisekiwa[j] <= x):ans += 1
if(Ruisekiwa[len(Ruisekiwa)-1] < x):ans -= 1
#print(Ruisekiwa)

print(ans)
    
