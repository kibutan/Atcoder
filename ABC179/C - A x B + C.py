N = int(input())
ans = 0
for i in range(1,N): #Cを決めてA*Bを決めたい
  for j in range(1,N+1): #A*B = N - i, A = j, B = (N-i)/j
    if(((N-i)/j).is_integer()):
      print("A:"+str(j)+", B:"+str((N-i)/j)+" C:"+str(i) + " AxB+C = "+str((j*((N-i)/j))+i))
      if(j != ((N-i)/j)):ans = ans + 2
      else:ans = ans + 1
print(ans)
