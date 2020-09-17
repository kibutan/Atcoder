N = int(input())
S = input()
if(len(S)<=N):print(S)
else:
  for i in range(N):
    print(S[i],end="")
  print("...")
