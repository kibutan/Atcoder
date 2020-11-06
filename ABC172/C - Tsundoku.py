N,M,K = list(map(int,input().split()))
A = list(map(int,input().split()))
Ruisekiwa_A = [0]*(N+1)
B = list(map(int,input().split()))
Ruisekiwa_B = [0]*(M+1)
for k in range(N):
  Ruisekiwa_A[k+1] = Ruisekiwa_A[k]+A[k]
print(Ruisekiwa_A)
for k in range(M):
  Ruisekiwa_B[k+1] = Ruisekiwa_B[k]+B[k]
print(Ruisekiwa_B)
ans = 0
j = 0
b_cnt = 0
for i in range(N+1): #List_Aは0から始まる
  b_cnt = max([j for j, x in enumerate(Ruisekiwa_B) if x <= (K-Ruisekiwa_A[i])])
  #Aを読む冊数を固定したときにBを何冊読むことができるかの計算式。
  #Bの累積和をAを読んだときの残時間を超えないものをリストアップ、そのインデックスを入れる
  print("---------")
  print("Aを読む冊数"+str(i))
  print("Timelimit:"+str(K))
  print("Aを読んだのち残る時間"+str((K-Ruisekiwa_A[i])))
  print("Bを読むのにかかる時間"+str((Ruisekiwa_B[b_cnt])))
  
  print("Bを読む冊数"+str(b_cnt))
  #Aの冊数とBの冊数が答え
  print("A+Bの冊数"+str(i + b_cnt))
  print("---------")  
  ans = max(ans, i+b_cnt)
print("final:",ans)
