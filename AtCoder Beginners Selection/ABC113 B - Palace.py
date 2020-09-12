N = int(input())
temp = [0 for m in range(N)]
T = list(map(int,input().split()))
A = T[1]
H = list(map(int,input().split()))

for i in range(N):
  temp[i] = T[i] - H[i] * 0.006
  print(temp[i])
  
  #2
  #12 5
  #1000 2000
